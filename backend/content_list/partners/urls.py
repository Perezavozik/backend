from rest_framework import routers

from content_list.partners.views import PartnerListViewSet

router = routers.DefaultRouter()
router.register(r'', PartnerListViewSet, basename='partners-gallery')
urlpatterns = router.urls
