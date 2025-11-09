from parler_rest.serializers import TranslatableModelSerializer

from about_us.models import About


class AboutSerializer(TranslatableModelSerializer):
    translation_fields = ['menu_title', 'title', 'body']
    class Meta:
        model = About
        fields = ('id', 'menu_title', 'title', 'body', 'order')
