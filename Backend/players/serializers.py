from rest_framework import serializers
from players.models import Player, PlayerScore, ProfileImage
from players.service import create_player


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileImage
        fields = ['thumbnail', 'med', 'large']


class PlayerScoreSerializer(serializers.ModelSerializer):
    last_match = serializers.StringRelatedField()

    class Meta:
        model = PlayerScore
        fields = ['amount', 'last_match']


class PlayerListRetrieveUpdateSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    profile_img = ProfileImageSerializer()
    score = PlayerScoreSerializer()

    class Meta:
        model = Player
        fields = ['UUID', 'nickname', 'score', 'date_joined', 'active', 'profile_img']


# TODO
class PlayerCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        player = create_player(validated_data)
        return player

    class Meta:
        model = Player
        fields = ['UUID', 'nickname']


class PlayerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['UUID', 'nickname']
