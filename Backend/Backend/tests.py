from django.test import TestCase
from Backend.service import new_and_existing_players_qty, create_new_players, \
    define_players, play_loop
from matches.models import Match, MatchScore
from players.models import Player, PlayerScore
from unittest.mock import patch
from players.service import create_player
from Backend.mock_api import mock_result, MockResponse


class TestBackendService(TestCase):

    @patch("Backend.service.randint")
    def test_new_and_existing_players_qty_only_existing(self, mock_random):
        mock_random.return_value = 0
        [create_player({"nickname": f"Test{i}"}) for i in range(1, 20)]

        existing_players, new_players_qty = new_and_existing_players_qty(10)
        self.assertEqual(10, existing_players)
        self.assertEqual(0, new_players_qty)

    @patch("Backend.service.randint")
    def test_new_and_existing_players_qty_only_new(self, mock_random):
        mock_random.return_value = 10
        existing_players, new_players_qty = new_and_existing_players_qty(10)
        self.assertEqual(0, existing_players)
        self.assertEqual(10, new_players_qty)

    @patch("Backend.service.randint")
    def test_new_and_existing_players_qty_mixed(self, mock_random):
        mock_random.return_value = 5
        [create_player({"nickname": f"Test{i}"}) for i in range(1, 20)]
        existing_players, new_players_qty = new_and_existing_players_qty(10)
        self.assertEqual(5, existing_players)
        self.assertEqual(5, new_players_qty)

    @patch("Backend.service.randint")
    def test_new_and_existing_players_qty_not_enough_existing(self, mock_random):
        mock_random.return_value = 3
        [create_player({"nickname": f"Test{i}"}) for i in range(1, 5)]
        existing_players, new_players_qty = new_and_existing_players_qty(10)
        self.assertEqual(4, existing_players)
        self.assertEqual(6, new_players_qty)

    @patch('Backend.service.requests.get')
    def test_create_new_players(self, mock_api):
        self.assertEqual(0, Player.objects.count())
        mock_api.return_value = MockResponse(mock_result(), 200)
        players = create_new_players(5)

        self.assertEqual(5, Player.objects.count())
        self.assertListEqual(players, list(Player.objects.all()))

    @patch('Backend.service.requests.get')
    @patch("Backend.service.new_and_existing_players_qty")
    @patch("Backend.service.randint")
    def test_define_players(self, mock_random, mock_quantities, mock_api):
        mock_random.return_value = 10
        mock_quantities.return_value = (5, 5)
        mock_api.return_value = MockResponse(mock_result(), 200)
        self.assertEqual(0, Player.objects.count())
        [create_player({"nickname": f"Test{i}"}) for i in range(1, 6)]
        players = set(define_players())

        self.assertEqual(10, Player.objects.count())
        self.assertSetEqual(players, set(Player.objects.all()))

    def test_play_loop(self):
        pass

    @patch('Backend.service.requests.get')
    @patch("Backend.service.new_and_existing_players_qty")
    @patch("Backend.service.randint")
    def test_play_loop(self, mock_random, mock_quantities, mock_api):
        mock_random.return_value = 10
        mock_quantities.return_value = (5, 5)
        mock_api.return_value = MockResponse(mock_result(), 200)
        [create_player({"nickname": f"Test{i}"}) for i in range(1, 8)]
        self.assertEqual(7, Player.objects.count())
        self.assertEqual(7, PlayerScore.objects.count())

        play_loop()
        self.assertEqual(12, Player.objects.count())
        self.assertEqual(12, PlayerScore.objects.count())
        self.assertEqual(1, Match.objects.count())
        self.assertIsNotNone(Match.objects.first().date_finished)
        self.assertEqual(10, MatchScore.objects.count())
        self.assertEqual(10, PlayerScore.objects.filter(amount__lte=100, amount__gte=1).count())

