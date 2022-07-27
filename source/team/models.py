from django.db import models

GENRE_CHOICES = (
    ('Masculino','Masculino'),
    ('Feminino', 'Feminino'),
    ('Misto','Misto'),
)

class TeamUser(models.Model):
    team = models.ForeignKey('team.Team', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)

class Modality(models.Model):
    
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=10,choices=GENRE_CHOICES, default='Misto')

    def __str__(self):
        return f"{self.name} - {self.genre}"

class Team(models.Model):
    
    modality = models.ForeignKey('team.Modality', on_delete=models.DO_NOTHING)
    athletic = models.ForeignKey('athletic.Athletic', on_delete=models.DO_NOTHING)
    players = models.ManyToManyField('accounts.User', through=TeamUser)

    def __str__(self):
        return f"{self.athletic} - {self.modality}"