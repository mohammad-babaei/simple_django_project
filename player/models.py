from django.db import models
from club.models import Club


class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, related_name="players", null=True)
