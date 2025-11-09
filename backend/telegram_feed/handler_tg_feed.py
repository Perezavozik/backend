# telegram_feed/simple_fetch.py
import os
from datetime import UTC

from telegram import Bot

BOT_TOKEN  = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("TG_CHANNEL_ID")        # "@my_channel" или -100…

bot = Bot(BOT_TOKEN)
_last_update_id: int | None = None


async def fetch_latest_posts(limit: int = 8) -> list[dict]:
    """
    Вернёт список последних `limit` постов канала/группы.
    Требует: бот админ, посты публикуются ПОСЛЕ добавления бота.
    """
    global _last_update_id

    updates = await bot.get_updates(offset=_last_update_id, timeout=0, limit=100)

    posts: list[dict] = []
    for upd in updates:
        msg = upd.channel_post or upd.edited_channel_post
        if not msg or str(msg.chat.id) not in {str(CHANNEL_ID), CHANNEL_ID.lstrip("@")}:
            continue

        photo_url = None
        if msg.photo:
            file_id = msg.photo[-1].file_id           # самая крупная картинка
            f = await bot.get_file(file_id)
            photo_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{f.file_path}"

        posts.append(
            {
                "id": msg.message_id,
                "text": msg.text_html or msg.caption_html or "",
                "photo_url": photo_url,
                "date": msg.date.astimezone(UTC).isoformat(),
            }
        )

    if updates:
        _last_update_id = updates[-1].update_id + 1

    posts.sort(key=lambda x: x["date"])
    return posts[-limit:]
