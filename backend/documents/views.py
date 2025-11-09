
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from documents.models import TypeDocument
from documents.serializers import DocumentTypeSerializer


class DocumentViewSet(mixins.ListModelMixin,
                         GenericViewSet):
    queryset = TypeDocument.objects.all().prefetch_related("documents").order_by("-order")
    serializer_class = DocumentTypeSerializer
