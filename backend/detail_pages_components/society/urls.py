from rest_framework.routers import DefaultRouter

from detail_pages_components.society.views import SocietyViewSet

router = DefaultRouter()
router.register(r'', SocietyViewSet, basename='society')

urlpatterns = router.urls
