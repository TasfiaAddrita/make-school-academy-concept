from django import forms
from wiki.models import Tutorial


class TutorialForm(forms.ModelForm):
    """ Render and process a form based on the Tutorial model. """
    class Meta:
        model = Tutorial
        # fields = '__all__'
        fields = ['title', 'description']
