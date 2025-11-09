from rest_framework.routers import DefaultRouter

from detail_pages_components.language.views import LanguageViewSet

router = DefaultRouter()
router.register(r'', LanguageViewSet, basename='society')

urlpatterns = router.urls
