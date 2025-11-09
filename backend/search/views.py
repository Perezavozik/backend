from django.conf import settings
from django.utils.translation import get_language
from rest_framework.response import Response
from rest_framework.views import APIView

from search.search_registry import SEARCH_MODELS


class GlobalSearchView(APIView):
    permission_classes = []

    def get(self, request):
        query = request.GET.get("q", "").strip()
        lang  = get_language() or settings.LANGUAGE_CODE

        results = []
        for model in SEARCH_MODELS:
            for row in model.search(query, lang):
                results.append({
                    "id": row["id"],
                    "title": row["translations__name"],
                    "announcement": row["translations__announcement"],
                    "slug": row["slug"],
                    "model": model._meta.model_name,
                    "image": (
                        request.build_absolute_uri(
                            f"{settings.MEDIA_URL}{row['image']}"
                        ) if row["image"] else None
                    ),
                })

        return Response(results)
