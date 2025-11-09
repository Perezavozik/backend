from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from about_us.models import About
from about_us.serializers import AboutSerializer


class AboutViewSet(mixins.ListModelMixin,
                         GenericViewSet):
    queryset = About.objects.all().order_by('-order')
    serializer_class = AboutSerializer
