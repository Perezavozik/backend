from rest_framework import routers

from media_library.views import MediaLibraryViewSet

router = routers.DefaultRouter()
router.register(r'', MediaLibraryViewSet, basename='media_library')
urlpatterns = router.urls
