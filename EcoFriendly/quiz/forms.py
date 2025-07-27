from django import forms
from quiz.models import Question

from django import forms
from .models import Question

#Question Form for Validation 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question', 'choice_a', 'choice_b', 'choice_c', 'choice_d',
            'correct_choice', 'explanation'
        ]
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'choice_a': forms.TextInput(attrs={'class': 'form-control'}),
            'choice_b': forms.TextInput(attrs={'class': 'form-control'}),
            'choice_c': forms.TextInput(attrs={'class': 'form-control'}),
            'choice_d': forms.TextInput(attrs={'class': 'form-control'}),
            'correct_choice': forms.Select(attrs={'class': 'form-select'}),
            'explanation': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }