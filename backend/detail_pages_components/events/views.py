from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from detail_pages_components.events.models import Event
from detail_pages_components.events.serializers import EventDetailSerializer, EventSerializer


class EventViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Event.objects.all().order_by('-order', '-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EventDetailSerializer
        else:
            return EventSerializer
