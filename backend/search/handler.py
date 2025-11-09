from django.db.models import Q


class SearchableMixin:
    search_fields = (
        "translations__name",
        "translations__announcement",
        "translations__description",
    )
    @classmethod
    def search(cls, query: str, language: str):

        if not query:
            return cls.objects.none()

        q_object = Q()
        for f in cls.search_fields:
            q_object |= Q(**{f + "__icontains": query})

        return (
            cls.objects
               .active_translations(language_code=language)
               .filter(q_object)
               .values(
                   "id",
                   "slug",
                   "image",
                   "translations__name",
                   "translations__announcement",
               )
        )
