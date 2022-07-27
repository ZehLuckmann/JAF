from django import forms
from .models import Tournament, Game

class TournamentForm(forms.ModelForm):
 
   class Meta:
        model = Tournament
 
        fields = [
            "name",
            "start",
            "end",
            "modalities"
        ]

        widgets = {
            'start': forms.DateInput(attrs={'class':'date-input'}),
            'end': forms.DateInput(attrs={'class':'date-input'}),
        }

class GameForm(forms.ModelForm):
     
   class Meta:
        model = Game
 
        fields = [
            "tournament",
            "modality",
            "team_1",
            "team_2",
            "date_time",
        ]

        
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'class':'datetime-input'})
        }
