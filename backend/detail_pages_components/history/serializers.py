from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.history.models import History


class HistorySerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement']

    class Meta:
        model = History
        fields = ("id", "name", "slug", "announcement", "image")

class HistoryDetailSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement', 'description']

    class Meta:
        model = History
        fields = ("id", "name", "description", "announcement", "image")
