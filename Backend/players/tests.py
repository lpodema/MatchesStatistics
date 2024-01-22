import random

from django.test import TestCase
from players.service import create_player, update_player_score, get_players_by_quantity, get_playerbase_number, get_player_from_str_uuid
from players.models import Player, PlayerScore, ProfileImage
from matches.service import create_match


class TestPlayerServiceOptimistic(TestCase):

    def test_create_player(self):
        self.assertEqual(0, Player.objects.count())
        player = create_player({"nickname": "test1"})
        self.assertEqual(1, Player.objects.count())
        self.assertEqual(player, Player.objects.first())
        self.assertEqual(1, PlayerScore.objects.filter(player=player).count())
        self.assertEqual(1, ProfileImage.objects.filter(player=player).count())

    def test_get_player_from_str_uuid(self):
        player = create_player({"nickname": "test1"})
        player_db = get_player_from_str_uuid(str(player.UUID))

        self.assertEqual(player, player_db)

    def test_update_score(self):
        match = create_match()
        player_list = [create_player({"nickname": f"Test{i}"}) for i in range(1, 11)]
        for player in player_list:
            update_player_score(player, random.randint(1, 100), match)

        self.assertEqual(0, PlayerScore.objects.filter(amount=0).count())

    def test_get_players_by_quantity(self):
        self.assertEqual(Player.objects.count(), get_playerbase_number())
        player_list = set([create_player({"nickname": f"Test{i}"}) for i in range(1, 11)])

        players_db = set(get_players_by_quantity(random.randint(5, 10)))

        intersection = players_db.intersection(player_list)
        self.assertSetEqual(players_db, intersection)
        self.assertEqual(Player.objects.count(), get_playerbase_number())


class TestPlayerServicePessimistic(TestCase):
    def test_update_score_concurrent(self):
        pass
        # TODO add concurrency to updating scores of any player
