import os
import re
import time
from html import unescape
from typing import Any

import django
import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.db import transaction

from .models import TelegramPost

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

EMOJI_PATTERN = re.compile(
    "[" "\U0001F600-\U0001F64F" "\U0001F300-\U0001F5FF" "\U0001F680-\U0001F6FF" "\U0001F1E0-\U0001F1FF" "\u2702-\u27B0" "\u24C2-\U0001F251" "]+",
    flags=re.UNICODE)
FLOOD_WAIT_RE = re.compile(r'FLOOD_WAIT_(\d+)', re.I)

_cache: dict[str, dict[str, Any]] = {}
_last_call_ts: float = 0.0
_MIN_GAP = 1.0


def is_sticker(msg: dict[str, Any]) -> bool:
    media = msg.get('media')
    if isinstance(media, dict) and media.get('_') == 'messageMediaDocument':
        doc = media.get('document', {})
        return doc.get('mime_type') == 'image/webp'
    return False


def parse_message(msg: dict[str, Any], channel: str) -> dict[str, Any]:
    raw_text = msg.get('message', '')
    clean_text = EMOJI_PATTERN.sub('', unescape(re.sub(r'<[^>]+>', '', raw_text))).strip()
    photo_url = None
    media = msg.get('media')
    if isinstance(media, dict) and media.get('_') == 'messageMediaPhoto':
        photo_url = f"https://tg.i-c-a.su/media/{channel.lstrip('@')}/{msg.get('id')}"
    post_url = f"https://t.me/{channel.lstrip('@')}/{msg.get('id')}"
    return {'post_id': msg.get('id'), 'text': clean_text, 'photo_url': photo_url, 'post_url': post_url}


def _fetch_json_with_backoff(url: str, retries: int = 4) -> dict[str, Any]:
    global _last_call_ts
    last_exc = None
    for attempt in range(retries):
        now = time.time()
        if now - _last_call_ts < _MIN_GAP:
            time.sleep(_MIN_GAP - (now - _last_call_ts))
        try:
            resp = requests.get(url, timeout=20)
            _last_call_ts = time.time()
            if resp.status_code in (420, 429):
                wait = 5
                m = FLOOD_WAIT_RE.search(resp.text) or FLOOD_WAIT_RE.search(getattr(resp, 'reason', '') or '')
                if m:
                    wait = int(m.group(1))
                time.sleep(wait + attempt * 0.5)
                continue
            if 500 <= resp.status_code < 600:
                time.sleep(1.0 * (2 ** attempt))
                continue
            resp.raise_for_status()
            return resp.json()
        except requests.HTTPError as e:
            last_exc = e
            status = e.response.status_code if e.response is not None else None
            if status in (420, 429):
                txt = ''
                try:
                    txt = e.response.text
                except Exception:
                    pass
                m = FLOOD_WAIT_RE.search(txt) or FLOOD_WAIT_RE.search(str(e))
                wait = int(m.group(1)) if m else 5
                time.sleep(wait + attempt * 0.5)
                continue
            if status and 500 <= status < 600:
                time.sleep(1.0 * (2 ** attempt))
                continue
            raise
        except requests.RequestException as e:
            last_exc = e
            time.sleep(0.8 * (attempt + 1))
            continue
    if last_exc:
        raise last_exc
    raise RuntimeError("Request failed after retries")


def _ext_from_content_type(ct: str | None) -> str:
    if not ct:
        return ".jpg"
    ct = ct.lower().split(";")[0].strip()
    if ct == "image/jpeg":
        return ".jpg"
    if ct == "image/png":
        return ".png"
    if ct == "image/webp":
        return ".webp"
    if ct == "image/gif":
        return ".gif"
    return ".jpg"


def _fetch_binary_with_backoff(url: str, retries: int = 4) -> tuple[bytes | None, str | None]:
    global _last_call_ts
    for attempt in range(retries):
        now = time.time()
        if now - _last_call_ts < _MIN_GAP:
            time.sleep(_MIN_GAP - (now - _last_call_ts))
        try:
            resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
            _last_call_ts = time.time()
            if resp.status_code in (420, 429):
                wait = 5
                m = FLOOD_WAIT_RE.search(resp.text) or FLOOD_WAIT_RE.search(getattr(resp, 'reason', '') or '')
                if m:
                    wait = int(m.group(1))
                time.sleep(wait + attempt * 0.5)
                continue
            if 500 <= resp.status_code < 600:
                time.sleep(1.0 * (2 ** attempt))
                continue
            resp.raise_for_status()
            return resp.content, resp.headers.get("Content-Type")
        except requests.HTTPError as e:
            status = e.response.status_code if e.response is not None else None
            if status in (420, 429):
                txt = ''
                try:
                    txt = e.response.text
                except Exception:
                    pass
                m = FLOOD_WAIT_RE.search(txt) or FLOOD_WAIT_RE.search(str(e))
                wait = int(m.group(1)) if m else 5
                time.sleep(wait + attempt * 0.5)
                continue
            if status and 500 <= status < 600:
                time.sleep(1.0 * (2 ** attempt))
                continue
            raise
        except requests.RequestException:
            time.sleep(0.8 * (attempt + 1))
            continue
    return None, None


def _abs_media_url(u: str) -> str:
    if u.startswith("http://") or u.startswith("https://"):
        return u
    base = getattr(settings, "SITE_BASE_URL", "").rstrip("/")
    if base:
        return base + u
    return u


def fetch_and_parse_telegram_posts(channel: str, limit: int = 8, max_fetch: int = 64) -> list[dict[str, Any]]:
    key = f"{channel}:{limit}"
    now = time.time()
    cached = _cache.get(key)
    if cached and now - cached['time'] < 86400:
        return cached['data']
    fetch_limit = max(limit * 2, 16)
    collected: list[dict[str, Any]] = []
    last_error = None
    while fetch_limit <= max_fetch and len(collected) < limit:
        try:
            url = f"https://tg.i-c-a.su/json/{channel.lstrip('@')}?limit={fetch_limit}"
            data = _fetch_json_with_backoff(url)
            msgs = data.get('messages') or data.get('result', {}).get('messages', []) or []
            parsed = [parse_message(m, channel) for m in msgs if 'message' in m and not is_sticker(m)]
            non_empty = [p for p in parsed if p.get('text') and p['text'].strip()]
            collected = non_empty[:limit]
            if len(collected) >= limit:
                break
        except Exception as e:
            last_error = e
        fetch_limit = min(int(fetch_limit * 1.5), max_fetch)
        time.sleep(0.5)
    if collected:
        _cache[key] = {'time': now, 'data': collected}
        return collected
    if cached:
        return cached['data']
    if last_error:
        raise last_error
    return []


def store_posts(channel: str, posts: list[dict[str, Any]]) -> int:
    def abs_media_url(u: str) -> str:
        if u.startswith(("http://", "https://")):
            return u
        base = getattr(settings, "SITE_BASE_URL", "").rstrip("/")
        return (base + u) if base else u

    with transaction.atomic():
        TelegramPost.objects.filter(channel=channel).delete()
        created = 0
        for p in posts:
            post = TelegramPost(
                channel=channel,
                post_id=p["post_id"],  # <- сохраняем
                text=p["text"],
                post_url=p["post_url"],
                photo_source_url=p.get("photo_url")  # исходник
            )
            post.save()
            if p.get("photo_url"):
                data, ct = _fetch_binary_with_backoff(p["photo_url"])
                if data:
                    ext = _ext_from_content_type(ct)
                    fname = f"{channel.lstrip('@')}_{p['post_id']}{ext}"
                    post.photo.save(fname, ContentFile(data), save=True)
                    post.photo_url = abs_media_url(post.photo.url)  # <- локальный абсолютный
                    post.save(update_fields=["photo", "photo_url"])
            created += 1
    return created


def fetch_and_store_telegram_posts(channel: str, limit: int = 8, max_fetch: int = 64) -> int:
    posts = fetch_and_parse_telegram_posts(channel, limit, max_fetch)
    return store_posts(channel, posts)
