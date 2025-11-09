from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from reports.models import Report
from reports.serializers import ReportSerializer


class ReportViewSet(mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Report.objects.all().order_by('-order')
    serializer_class = ReportSerializer
