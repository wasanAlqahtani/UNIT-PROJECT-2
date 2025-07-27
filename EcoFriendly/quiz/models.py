from django.db import models

# Create your models here.

#Question Model 
class Question(models.Model):
    class AnswerChoices(models.TextChoices):
        ANSWERA = 'A', 'A'
        ANSWERB = 'B', 'B'
        ANSWERC = 'C', 'C'
        ANSWERD = 'D', 'D'

    question = models.TextField()
    choice_a = models.CharField(max_length=255, default="Not provided")
    choice_b = models.CharField(max_length=255, default="Not provided")
    choice_c = models.CharField(max_length=255, default="Not provided")
    choice_d = models.CharField(max_length=255, default="Not provided")
    correct_choice = models.CharField(max_length=1, choices=AnswerChoices.choices)
    explanation = models.TextField(blank=True, null=True)

    



