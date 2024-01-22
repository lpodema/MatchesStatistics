from rest_framework import serializers
from matches.models import Match, MatchScore
from players.serializers import PlayerRetrieveSerializer


class MatchListRetrieveSerializer(serializers.ModelSerializer):
    players = PlayerRetrieveSerializer(many=True)

    class Meta:
        model = Match
        fields = ['UUID', 'players', 'date_finished']


class MatchUpdateSerializer(serializers.ModelSerializer):
    players = PlayerRetrieveSerializer(many=True)

    class Meta:
        model = Match
        fields = ['players']


# TODO
class MatchCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ['UUID', 'date_created']


class MatchScoreListRetrieveUpdateSerializer(serializers.ModelSerializer):
    player = PlayerRetrieveSerializer()
    match = MatchListRetrieveSerializer()

    class Meta:
        model = MatchScore
        fields = ['match', 'player', 'points']


# TODO
class MatchScoreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'
