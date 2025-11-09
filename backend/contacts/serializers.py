from rest_framework import serializers

from .models import PhonesContacts, SiteContacts


class PhoneContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonesContacts
        fields = ("phone",)

class SiteContactsSerializer(serializers.ModelSerializer):
    phones = PhoneContactSerializer(many=True, read_only=True)

    class Meta:
        model  = SiteContacts
        fields = ("email", "address", "working_time", "phones")
