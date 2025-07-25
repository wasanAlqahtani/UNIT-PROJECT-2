from django import forms
from eco.models import Action

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Title',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Description',
                'required': True
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            # location will be rendered manually as radios
        }
