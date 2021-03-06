from django import forms
from tutorials.models import Tutorial, Module, SubModule


class TutorialForm(forms.ModelForm):
    """ Render and process a form based on the Tutorial model. """
    class Meta:
        model = Tutorial
        # fields = '__all__'
        fields = ['title', 'description', 'cover_photo']
    
    def __init__(self, *args, **kwargs):
        super(TutorialForm, self).__init__(*args, **kwargs)
        self.fields['cover_photo'].required = False

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = ('tutorial',)