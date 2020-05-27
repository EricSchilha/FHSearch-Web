from django.db import models

class Stats(models.Model):
    rank = models.IntegerField(blank=True, null=False, primary_key=True)
    player = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=3, blank=True, null=True)
    position = models.CharField(max_length=2, blank=True, null=True)
    gamesplayed = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    plusminus = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    pointshares = models.FloatField(blank=True, null=True)
    evgoals = models.IntegerField(blank=True, null=True)
    ppgoals = models.IntegerField(blank=True, null=True)
    shgoals = models.IntegerField(blank=True, null=True)
    gwgoals = models.IntegerField(blank=True, null=True)
    evassists = models.IntegerField(blank=True, null=True)
    ppassists = models.IntegerField(blank=True, null=True)
    shassists = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    shootingpercentage = models.FloatField(blank=True, null=True)
    toi = models.IntegerField(blank=True, null=True)
    atoi = models.CharField(max_length=5, blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    faceoffwins = models.IntegerField(blank=True, null=True)
    faceofflosses = models.IntegerField(blank=True, null=True)
    faceoffwinpercentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'