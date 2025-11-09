from rest_framework.routers import DefaultRouter

from detail_pages_components.news_on_main.views import NewsOnMainViewSet

router = DefaultRouter()
router.register(r'', NewsOnMainViewSet, basename='news-on-main')

urlpatterns = router.urls
