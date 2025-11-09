from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from detail_pages_components.awards.models import Award
from detail_pages_components.awards.serializers import AwardsDetailSerializer, AwardsSerializer


class AwardsViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardsSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Award.objects.all().order_by('-order', '-id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AwardsDetailSerializer
        else:
            return AwardsSerializer
