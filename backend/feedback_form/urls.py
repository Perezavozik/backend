from rest_framework import routers

from feedback_form.views import FeedbackFormViewSet

router = routers.DefaultRouter()
router.register(r'', FeedbackFormViewSet, basename='feedback-form')
urlpatterns = router.urls
