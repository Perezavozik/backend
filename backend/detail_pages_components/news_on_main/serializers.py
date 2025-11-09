from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.news_on_main.models import NewsOnMain


class NewsOnMainSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement']

    class Meta:
        model = NewsOnMain
        fields = ("id", "name", "slug", "announcement", "image")

class NewsOnMainDetailSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement', 'description']

    class Meta:
        model = NewsOnMain
        fields = ("id", "name", "description", "announcement", "image")
