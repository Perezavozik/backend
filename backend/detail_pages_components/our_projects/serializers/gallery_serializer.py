from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.our_projects.models import OurProject


class OurProjectsGallerySerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement']

    class Meta:
        model = OurProject
        fields = ("id", "name", "slug", "announcement", "image")

class OurProjectDetailSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'description', 'announcement']
    class Meta:
        model = OurProject
        fields = ("id", "name", "announcement", "description", "image")
