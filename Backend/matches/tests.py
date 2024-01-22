from django.test import TestCase
from matches.service import create_match, join_match, finish_match
from matches.models import Match, MatchScore
from players.service import create_player


class TestMatchServiceOptimistic(TestCase):

    def test_create_match(self):
        self.assertEqual(0, Match.objects.count())
        match = create_match()
        match.refresh_from_db()
        self.assertIsInstance(match, Match)
        self.assertEqual(1, Match.objects.count())
        self.assertEqual(match, Match.objects.first())
        self.assertEqual(0, MatchScore.objects.filter(match=match).count())

    def test_join_match(self):
        match = create_match()
        player1 = create_player({"nickname": "Test1"})
        player2 = create_player({"nickname": "Test2"})
        join_match(match, player1)
        join_match(match, player2)

        match.refresh_from_db()
        self.assertIsInstance(match, Match)
        self.assertEqual(None, match.date_finished)
        self.assertEqual(2, match.players.count())
        self.assertEqual(0, MatchScore.objects.filter(match=match).count())

    def test_finish_match(self):
        match = create_match()
        player_list = [create_player({"nickname": f"Test{i}"}) for i in range(1, 11)]
        for player in player_list:
            join_match(match, player)
        match.refresh_from_db()
        self.assertIsInstance(match, Match)
        self.assertEqual(None, match.date_finished)
        self.assertEqual(10, match.players.count())
        self.assertEqual(0, MatchScore.objects.filter(match=match).count())

        finish_match(match)
        match.refresh_from_db()
        self.assertIsNotNone(match.date_finished)
        self.assertEqual(10, match.players.count())
        self.assertEqual(10, MatchScore.objects.filter(match=match).count())
        self.assertEqual(10, MatchScore.objects.filter(match=match, points__gte=1, points__lte=100).count())
        self.assertEqual(1, Match.objects.count())
        self.assertEqual(0, Match.objects.filter(date_finished=None).count())


class TestMatchServicePessimistic(TestCase):

    def test_join_match_full(self):
        match = create_match()
        player_list = [create_player({"nickname": f"Test{i}"}) for i in range(1, 20)]

        with self.assertRaises(Exception) as ex:
            for player in player_list:
                join_match(match, player)
        self.assertEqual("Matches are up to 10 players", ex.exception.__str__())

        match.refresh_from_db()
        self.assertIsInstance(match, Match)
        self.assertEqual(None, match.date_finished)
        self.assertEqual(10, match.players.count())
        self.assertEqual(0, MatchScore.objects.filter(match=match).count())

    # TODO add concurrency tests to check possible race conditions.
    def test_join_match_concurrent(self):
        pass
        # TODO: concurrent join match

    def test_finish_match_concurrent(self):
        pass
        # TODO: concurrent finish match
