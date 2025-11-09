from rest_framework.routers import DefaultRouter

from telegram_feed.views import TelegramFeedViewSet

router = DefaultRouter()
router.register(r"", TelegramFeedViewSet, basename="tg-feed")

urlpatterns = router.urls
