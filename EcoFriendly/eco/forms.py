from django import forms
from eco.models import Action

# Create the form class.
class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = "__all__"