from django import forms
from .models import Athletic
 
 # creating a form
class AthleticForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Athletic
 
        # specify fields to be used
        fields = [
            "initials",
            "name",
            "logo",
        ]