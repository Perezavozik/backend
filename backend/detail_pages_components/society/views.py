from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from detail_pages_components.society.models import Society
from detail_pages_components.society.serializers import SocietyDetailSerializer, SocietySerializer


class SocietyViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Society.objects.all().order_by('-order', '-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SocietyDetailSerializer
        else:
            return SocietySerializer
