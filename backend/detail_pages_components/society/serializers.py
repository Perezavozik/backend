from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.society.models import Society


class SocietySerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement']

    class Meta:
        model = Society
        fields = ("id", "name", "slug", "announcement", "image")

class SocietyDetailSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement', 'description']

    class Meta:
        model = Society
        fields = ("id", "name", "description", "announcement", "image")
