from players.models import Player, PlayerScore, ProfileImage
from django.db import transaction
from Backend.helper_functions import parse_uuid
from django.core.exceptions import ObjectDoesNotExist


def create_player(player_data):
    with transaction.atomic():
        player = Player.objects.create(nickname=player_data['nickname'])
        PlayerScore.objects.create(player=player)
        ProfileImage.objects.create(player=player)
        return player


def update_player_score(player, newscore, match):
    with transaction.atomic():
        player_score = PlayerScore.objects.select_for_update().get(player=player)
        player_score.amount += newscore
        player_score.last_match = match
        player_score.save()


def get_player_from_str_uuid(player_uuid):
    try:
        uuid = parse_uuid(player_uuid)
        player = Player.objects.get(UUID=uuid)
        return player
    # TODO
    except ValueError as ve:
        print(ve)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist


def get_players_by_quantity(quantity):
    return Player.objects.filter(active=True).order_by('?')[:quantity]


def get_playerbase_number():
    return Player.objects.count()
