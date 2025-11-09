from django.core.cache import cache
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from detail_pages_components.our_projects.models import OurProject
from detail_pages_components.our_projects.serializers.gallery_serializer import (
    OurProjectDetailSerializer,
    OurProjectsGallerySerializer,
)


class OurProjectsViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = OurProject.objects.all()
    serializer_class = OurProjectsGallerySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return OurProject.objects.all().order_by('-order', '-id')

    def list(self, request, *args, **kwargs):
        cache_key = "our_projects_gallery"
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = serializer.data
        cache.set(cache_key, response, timeout=60 * 60 * 24 * 7)
        return Response(response)

    def retrieve(self, request, *args, **kwargs):
        cache_key = "our_projects_detail"
        cache_data = cache.get(cache_key)
        if cache_data:
            return Response(cache_data)

        queryset = self.get_object()
        serializer = OurProjectDetailSerializer(instance=queryset)
        response = serializer.data
        cache.set(cache_key, response, timeout=60 * 60 * 24 * 7)
        return Response(response)
