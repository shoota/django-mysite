from django import forms
from .models import ClubTeam


class ClubTeamForm(forms.ModelForm):
    class Meta:
        model = ClubTeam
        fields = ('name', 'location',)