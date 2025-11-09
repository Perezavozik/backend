from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from media_library.models import MediaLibrary
from media_library.serializers import MediaLibrarySerializer


class MediaLibraryViewSet(mixins.ListModelMixin,
                         GenericViewSet):
    queryset = MediaLibrary.objects.all()
    serializer_class = MediaLibrarySerializer

    def get_queryset(self):
        return MediaLibrary.objects.all().order_by("-id")
