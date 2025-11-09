from parler_rest.serializers import TranslatableModelSerializer

from reports.models import Report


class ReportSerializer(TranslatableModelSerializer):
    translation_fields = ['menu_title', 'title', 'body']

    class Meta:
        model = Report
        fields = ('id', 'menu_title', 'title', 'body', 'order')
