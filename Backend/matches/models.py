import uuid
from django.db import models
from players.models import Player


class Match(models.Model):
    UUID = models.UUIDField(unique=True, db_index=True, editable=False, default=uuid.uuid4)
    players = models.ManyToManyField(Player, related_name="players")
    date_created = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateTimeField(null=True)

    def __str__(self):
        return f'{str(self.UUID)} played on {str(self.date_finished)}'

    class Meta:
        app_label = "matches"


class MatchScore(models.Model):
    points = models.PositiveSmallIntegerField(default=1)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('player', 'match')
        app_label = 'matches'
