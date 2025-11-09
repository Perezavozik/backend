
from django.db.models import F
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from detail_pages_components.awards_candidate.models import Candidate, CandidateAwards
from detail_pages_components.awards_candidate.serializers import (
    AwardCandidateDetailSerializer,
    AwardCandidateSerializer,
)


class CandidateAwardsViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         GenericViewSet):
    queryset = CandidateAwards.objects.all()
    serializer_class = AwardCandidateSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AwardCandidateDetailSerializer
        else:
            return AwardCandidateSerializer

    @action(detail=True, methods=['POST'])
    def vote(self, request, slug=None):
        award = self.get_object()
        candidate_id = request.data.get('candidate_id')
        if not candidate_id:
            return Response(
                {"detail": "candidate_id is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            candidate = award.candidates.get(pk=candidate_id)
        except Candidate.DoesNotExist:
            return Response(
                {"detail": "Candidate not found for this award."},
                status=status.HTTP_404_NOT_FOUND
            )

        Candidate.objects.filter(pk=candidate.pk).update(
            number_of_votes=F('number_of_votes') + 1
        )
        candidate.refresh_from_db(fields=['number_of_votes'])

        return Response(
            {
                "candidate_id": candidate.pk,
                "number_of_votes": candidate.number_of_votes
            },
            status=status.HTTP_200_OK
        )
    @action(detail=True, methods=['get'], url_path='recent')
    def recent(self, request, slug=None):
        current = self.get_object()
        qs = CandidateAwards.objects\
            .exclude(pk=current.pk)\
            .order_by('-id')[:6]
        serializer = AwardCandidateSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)
