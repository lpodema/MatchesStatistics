from random import randint
from matches.models import Match, MatchScore
from players.service import update_player_score
from django.db import transaction
from django.utils import timezone


def create_match(**kwargs):
    return Match.objects.create()


def join_match(match, player):
    # FIXME CHECK FOR RACE CONDITIONS.
    with transaction.atomic():
        match = Match.objects.select_for_update().get(UUID=match.UUID)
        # TODO make thread-safe. select_for_update locks related models' rows
        if match.players.count() > 9:
            raise Exception("Matches are up to 10 players")
        match.players.add(player)


def finish_match(match):
    match_scores = []
    with transaction.atomic():
        match = Match.objects.select_for_update().get(UUID=match.UUID, date_finished=None)
        match.date_played = timezone.now()
        players = match.players.all()
        # FIXME Check the locking of update of scores. possible race conditions.
        for player in players:
            points = randint(1, 100)
            match_scores.append(MatchScore(player=player, points=points, match=match))
            update_player_score(player, points, match)

        MatchScore.objects.bulk_create(match_scores)
        match.date_finished = timezone.now()
        match.save()
