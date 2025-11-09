from rest_framework.routers import DefaultRouter

from detail_pages_components.culture.views import CultureViewSet

router = DefaultRouter()
router.register(r'', CultureViewSet, basename='society')

urlpatterns = router.urls
