# views.py
from datetime import datetime, time, date
from typing import List, Tuple

from django.conf import settings
from django.db.models import F, Q, Value
from django.db.models.functions import Coalesce
from django.utils.timezone import make_aware
from django.utils.translation import get_language
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import F, Value
from detail_pages_components.news_on_main.models import NewsOnMain
from detail_pages_components.news_on_main.serializers import (
    NewsOnMainDetailSerializer,
    NewsOnMainSerializer,
)
from django.db.models.functions import Coalesce, Cast
from django.db.models import DateTimeField

from detail_pages_components.awards.models import Award
from detail_pages_components.culture.models import Culture
from detail_pages_components.events.models import Event
from detail_pages_components.history.models import History
from detail_pages_components.language.models import Language
from detail_pages_components.our_projects.models import OurProject
from detail_pages_components.society.models import Society


FEED_MODELS: List[Tuple[type, List[str]]] = [
    (NewsOnMain,  ["published_at", "date", "created_at", "updated_at"]),
    (Event,       ["date", "start_at", "published_at", "created_at"]),
    (Award,       ["published_at", "date", "created_at"]),
    (Culture,     ["published_at", "date", "created_at"]),
    (History,     ["published_at", "date", "created_at"]),
    (Language,    ["published_at", "date", "created_at"]),
    (OurProject,  ["published_at", "date", "created_at"]),
    (Society,     ["published_at", "date", "created_at"]),
]


class NewsOnMainViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = NewsOnMain.objects.all()
    serializer_class = NewsOnMainSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return NewsOnMain.objects.all().order_by('-order', '-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NewsOnMainDetailSerializer
        return NewsOnMainSerializer

    def list(self, request, *args, **kwargs):
        lang = get_language() or settings.LANGUAGE_CODE

        try:
            limit = int(request.query_params.get("limit", "0"))
        except ValueError:
            limit = 0

        feed = []

        for Model, date_fields in FEED_MODELS:
            qs = Model.objects.all()
            if hasattr(Model.objects, "active_translations"):
                qs = Model.objects.active_translations(language_code=lang)

            # собрать список реально существующих полей даты
            existing_date_fields = []
            for f in date_fields:
                try:
                    Model._meta.get_field(f)
                    existing_date_fields.append(f)
                except Exception:
                    continue
            if not existing_date_fields:
                continue

            # аннотация pub_date: один столбец — F(...), несколько — Coalesce(...)
            if len(existing_date_fields) == 1:
                qs = qs.annotate(
                    pub_date=Cast(F(existing_date_fields[0]), output_field=DateTimeField())
                )
            else:
                qs = qs.annotate(
                    pub_date=Coalesce(
                        *[Cast(F(f), output_field=DateTimeField()) for f in existing_date_fields],
                        output_field=DateTimeField(),
                    )
                )
            qs = qs.values(
                "id",
                "slug",
                "image",
                "translations__name",
                "translations__announcement",
                "pub_date",
            )

            for row in qs:
                dt = row.get("pub_date")
                # Нормализуем date -> datetime для корректной сортировки
                if isinstance(dt, date) and not isinstance(dt, datetime):
                    dt = datetime.combine(dt, time.min)

                feed.append({
                    "id": row["id"],
                    "title": row["translations__name"],
                    "announcement": row["translations__announcement"],
                    "slug": row["slug"],
                    "model": Model._meta.model_name,
                    "image": (
                        request.build_absolute_uri(f"{settings.MEDIA_URL}{row['image']}")
                        if row.get("image") else None
                    ),
                    "date": dt,
                })

        # Сортировка: None в конец, свежие — наверх
        feed.sort(key=lambda x: (x["date"] is not None, x["date"]), reverse=True)

        if limit and limit > 0:
            feed = feed[:limit]

        return Response(feed)