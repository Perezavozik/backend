
from django.urls import path

from contacts.views import SiteContactsView

urlpatterns = [
    path("", SiteContactsView.as_view(), name="site-contacts"),
]
