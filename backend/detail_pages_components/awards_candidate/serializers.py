from rest_framework import serializers

from detail_pages_components.awards_candidate.models import Candidate, CandidateAwards


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ("id", "name", "description", "photo")


class AwardCandidateDetailSerializer(serializers.ModelSerializer):
    candidates = CandidateSerializer(many=True, read_only=True)
    class Meta:
        model = CandidateAwards
        fields = ("name", "description", "candidates", "image")


class AwardCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateAwards
        fields = ("name", "description", "image", "slug")
