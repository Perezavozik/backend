from rest_framework.routers import DefaultRouter

from detail_pages_components.events.views import EventViewSet

router = DefaultRouter()
router.register(r'', EventViewSet, basename='events')

urlpatterns = router.urls
