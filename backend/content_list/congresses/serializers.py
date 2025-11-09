from parler_rest.serializers import TranslatableModelSerializer

from content_list.congresses.models import Congresses


class CongressesSerializer(TranslatableModelSerializer):
    translation_fields = ['menu_title', 'title', 'body']
    class Meta:
        model = Congresses
        fields = ("menu_title", "title", "body", "order")
