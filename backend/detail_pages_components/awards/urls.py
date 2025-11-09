from rest_framework.routers import DefaultRouter

from detail_pages_components.awards.views import AwardsViewSet

router = DefaultRouter()
router.register(r'', AwardsViewSet, basename='awards')

urlpatterns = router.urls
