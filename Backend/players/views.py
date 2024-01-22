from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from players.models import Player, PlayerScore, ProfileImage
from players.serializers import PlayerListRetrieveUpdateSerializer, PlayerCreateSerializer, \
    ProfileImageSerializer, PlayerScoreSerializer


class PlayerListRetrieveUpdateViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Player.objects.all().order_by('-score__amount')
    serializer_class = PlayerListRetrieveUpdateSerializer
    lookup_field = 'UUID'


# TODO
class PlayerCreateViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = PlayerCreateSerializer


# TODO
class PlayerScoreViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer


# TODO
class ProfileImageViewSet(ModelViewSet):
    serializer_class = ProfileImageSerializer
    queryset = ProfileImage.objects.all()
