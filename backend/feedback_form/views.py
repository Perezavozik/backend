from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from feedback_form.models import FeedbackForm
from feedback_form.serializers import FeedbackSerializer


class FeedbackFormViewSet(mixins.CreateModelMixin,
                         GenericViewSet):
    serializer_class = FeedbackSerializer
    queryset = FeedbackForm.objects.all()
