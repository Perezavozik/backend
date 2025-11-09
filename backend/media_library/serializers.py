from rest_framework import serializers

from media_library.models import MediaLibrary


class MediaLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLibrary
        fields = ("image", )
