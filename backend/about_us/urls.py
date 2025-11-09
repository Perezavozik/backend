from rest_framework import routers

from about_us.views import AboutViewSet

router = routers.DefaultRouter()
router.register(r'', AboutViewSet, "congresses")

urlpatterns = router.urls
