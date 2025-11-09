from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.awards.models import Award


class AwardsSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement']

    class Meta:
        model = Award
        fields = ("id", "name", "slug", "announcement", "image")


class AwardsDetailSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement', 'description']

    class Meta:
        model = Award
        fields = ("id", "name", "description", "announcement", "image")
