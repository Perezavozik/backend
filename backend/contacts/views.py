from rest_framework import generics

from contacts.models import SiteContacts
from contacts.serializers import SiteContactsSerializer


class SiteContactsView(generics.RetrieveAPIView):
    serializer_class = SiteContactsSerializer

    def get_object(self):
        return SiteContacts.get_solo()
