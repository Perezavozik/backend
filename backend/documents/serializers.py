from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from documents.models import Document, TypeDocument


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("title", "file")


class DocumentTypeSerializer(TranslatableModelSerializer):
    translation_fields = ['title', 'description']
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = TypeDocument
        fields = ("title", "description", "documents", "order")
