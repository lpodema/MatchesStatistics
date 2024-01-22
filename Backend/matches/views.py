from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from matches.models import Match, MatchScore
from matches.serializers import MatchListRetrieveSerializer, \
    MatchCreateSerializer, MatchUpdateSerializer, \
    MatchScoreListRetrieveUpdateSerializer, MatchScoreCreateSerializer
from matches.service import join_match, finish_match
from rest_framework.response import Response
from rest_framework import status
from Backend.service import play_loop
from players.service import get_player_from_str_uuid


class MatchListRetrieveViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchListRetrieveSerializer
    lookup_field = 'UUID'


class MatchUpdateViewset(UpdateModelMixin, GenericViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchUpdateSerializer
    lookup_field = 'UUID'

    def update(self, request, *args, **kwargs):
        players = self.request.data.pop('players')
        match = self.get_object()
        nicknames = ''
        for player in players:
            # FIXME
            player = get_player_from_str_uuid(player['UUID'])
            join_match(match, player)
            nicknames += player['nickname'] + ', '

        return Response(data={'message': f"players {nicknames.rstrip()} joined successfully"}, status=status.HTTP_200_OK)


# TODO
class MatchCreateViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = MatchCreateSerializer


class MatchPlayScriptAPI(APIView):
    def post(self, request):
        play_loop()
        return Response(data={"message": "Match played succesfully"}, status=status.HTTP_200_OK)


class MatchFinishViewSet(UpdateModelMixin, GenericViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchUpdateSerializer
    lookup_field = 'UUID'

    def update(self, request, *args, **kwargs):
        match = self.get_object()
        if not match.date_finished:
            finish_match(match)
            return Response(data={"message": "Match finished successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Match has already finished"}, status=status.HTTP_400_BAD_REQUEST)


# TODO
class MatchScoreCreateViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = MatchScoreCreateSerializer


class MatchScoreListViewSet(ListModelMixin, GenericViewSet):
    queryset = MatchScore.objects.all()
    serializer_class = MatchScoreListRetrieveUpdateSerializer


class MatchScoreRetrieveUpdateViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = MatchScoreListRetrieveUpdateSerializer

    def get_queryset(self):
        match_id = self.request.parser_context.get('kwags').get('match')
        return MatchScore.objects.filter(match__uuid=match_id)
