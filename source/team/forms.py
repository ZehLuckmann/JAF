from django import forms
from .models import Modality, Team, TeamUser
 
class ModalityForm(forms.ModelForm):
     
    class Meta:
        model = Modality
        fields = [
            "name",
            "genre",
        ]

class TeamForm(forms.ModelForm):
 
    class Meta:
        model = Team
 
        fields = [
            "athletic",
            "modality",
        ]

class TeamUserForm(forms.ModelForm):
     
    class Meta:
        model = TeamUser
 
        fields = [
            "team",
            "user",
        ]