from rest_framework.routers import DefaultRouter

from detail_pages_components.awards_candidate.views import CandidateAwardsViewSet

router = DefaultRouter()
router.register(r'', CandidateAwardsViewSet, basename='awards_candidate')

urlpatterns = router.urls
