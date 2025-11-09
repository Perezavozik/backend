from rest_framework.routers import DefaultRouter

from detail_pages_components.history.views import HistoryViewSet

router = DefaultRouter()
router.register(r'', HistoryViewSet, basename='society')

urlpatterns = router.urls
