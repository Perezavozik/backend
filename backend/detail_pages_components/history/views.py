from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from detail_pages_components.history.models import History
from detail_pages_components.history.serializers import HistoryDetailSerializer, HistorySerializer


class HistoryViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return History.objects.all().order_by('-order', '-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return HistoryDetailSerializer
        else:
            return HistorySerializer
