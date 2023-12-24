from django import forms
from django.forms import ModelForm


class TeamForm(ModelForm):
    id_pokemon = forms.CharField(label='id_pokemon')

    class Meta:
        fields = ('id_pokemon',)
