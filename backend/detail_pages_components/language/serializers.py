from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.language.models import Language


class LanguageSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement']

    class Meta:
        model = Language
        fields = ("id", "name", "slug", "announcement", "image")

class LanguageDetailSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement', 'description']

    class Meta:
        model = Language
        fields = ("id", "name", "description", "announcement", "image")
