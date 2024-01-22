import uuid
from django.db import models
from Backend.settings.dev import PROFILE_IMG


class Player(models.Model):
    UUID = models.UUIDField(unique=True, db_index=True, editable=False, default=uuid.uuid4)
    date_joined = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=255, db_index=True, unique=True)
    active = models.BooleanField(default=True)

    def delete(self):
        self.active = False
        self.save()

    class Meta:
        app_label = "players"


def route(instance, filename):
    return f'{PROFILE_IMG}/{str(instance.player.UUID)}/{filename}'


class ProfileImage(models.Model):
    player = models.OneToOneField(Player, primary_key=True, on_delete=models.CASCADE,
                                  related_name="profile_img")
    thumbnail = models.ImageField(upload_to=route)
    med = models.ImageField(upload_to=route)
    large = models.ImageField(upload_to=route)

    class Meta:
        app_label = "players"


class PlayerScore(models.Model):
    player = models.OneToOneField(Player, primary_key=True, on_delete=models.CASCADE, related_name="score")
    amount = models.PositiveBigIntegerField(default=0)
    last_match = models.ForeignKey('matches.Match', on_delete=models.PROTECT, null=True)

    class Meta:
        app_label = "players"
