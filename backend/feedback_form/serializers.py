from rest_framework import serializers

from feedback_form.models import FeedbackForm


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = ("name", "email", "phone", "message")
