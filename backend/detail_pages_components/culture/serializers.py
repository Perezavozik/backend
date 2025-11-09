from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.culture.models import Culture


class CultureSerializer(TranslatableModelSerializer):
    translation_fields = ["name", "announcement"]

    class Meta:
        model = Culture
        fields = ("id", "name", "slug", "announcement", "image")

class CultureDetailSerializer(TranslatableModelSerializer):
    translation_fields = ["name", "announcement", "description"]

    class Meta:
        model = Culture
        fields = ("id", "name", "description", "announcement", "image")
