from django.conf import settings
from django.db import models


class Quests(models.Model):
    "Generated Model"
    completion = models.BooleanField()
    quest_id = models.BigIntegerField(
        null=True,
        blank=True,
    )


class Standings(models.Model):
    "Generated Model"
    rank = models.PositiveIntegerField()
    completion_percent = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )


class User_Quest_Join(models.Model):
    "Generated Model"
    user_id = models.BigIntegerField()
    quest_id = models.BigIntegerField()
