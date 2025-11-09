from django.core.cache import cache
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from content_list.partners.models import Partners
from content_list.partners.serializers import PartnersSerializer


class PartnerListViewSet(mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

    def get_queryset(self):
        return Partners.objects.all().order_by('-order')


    def list(self, request, *args, **kwargs):
        cache_key = "partners-data"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        cache.set(cache_key, data, timeout=60 * 60 * 24 * 7)
        return Response(data)
