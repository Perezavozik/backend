from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from content_list.congresses.models import Congresses
from content_list.congresses.serializers import CongressesSerializer


class CongressViewSet(mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Congresses.objects.all().order_by('-order')
    serializer_class = CongressesSerializer
