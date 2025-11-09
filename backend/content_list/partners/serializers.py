from rest_framework import serializers

from content_list.partners.models import Partners


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'
