from django.db import models


class TournamentModality(models.Model):
    tournament = models.ForeignKey('tournament.Tournament', on_delete=models.DO_NOTHING)
    modality = models.ForeignKey('team.Modality', on_delete=models.DO_NOTHING)

class Tournament(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60)
    start = models.DateTimeField()
    end = models.DateTimeField()
    modalities = models.ManyToManyField('team.Modality', through=TournamentModality)

    def __str__(self):
        return self.name

class Game(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    tournament = models.ForeignKey('tournament.Tournament', on_delete=models.DO_NOTHING)
    modality = models.ForeignKey('team.Modality', on_delete=models.DO_NOTHING)
    team_1 = models.ForeignKey('team.Team', on_delete=models.DO_NOTHING,related_name='%(class)s_team_1')
    team_2 = models.ForeignKey('team.Team', on_delete=models.DO_NOTHING,related_name='%(class)s_team_2')
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name