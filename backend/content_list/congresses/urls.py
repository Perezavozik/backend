from rest_framework import routers

from content_list.congresses.views import CongressViewSet

router = routers.DefaultRouter()
router.register(r'', CongressViewSet, "congresses")

urlpatterns = router.urls
