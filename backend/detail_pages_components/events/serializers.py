from parler_rest.serializers import TranslatableModelSerializer

from detail_pages_components.events.models import Event


class EventSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement']

    class Meta:
        model = Event
        fields = ("id", "name", "slug", "announcement", "image", "date", "place")

class EventDetailSerializer(TranslatableModelSerializer):
    translation_fields = ['name', 'announcement', 'description']

    class Meta:
        model = Event
        fields = ("id", "name", "description", "announcement", "image", "date", "place")
