from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from detail_pages_components.culture.models import Culture
from detail_pages_components.culture.serializers import CultureDetailSerializer, CultureSerializer


class CultureViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Culture.objects.all().order_by('-order', '-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CultureDetailSerializer
        else:
            return CultureSerializer
