from rest_framework import routers

from reports.views import ReportViewSet

router = routers.DefaultRouter()
router.register(r'', ReportViewSet, "congresses")

urlpatterns = router.urls
