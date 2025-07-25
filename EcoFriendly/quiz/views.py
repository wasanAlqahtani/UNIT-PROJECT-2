from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Question
from .forms import QuestionForm

# Create your views here.
def all_question_view(request:HttpRequest):
    questions = Question.objects.all()
    return render(request, 'quiz/all_questions.html', {"questions":questions})

def add_question_view(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quiz:add_question_view') 
        
    return render(request, 'quiz/add_question.html', {'form': form ,"AnswerChoices": Question.AnswerChoices.choices})

def delete_view(request:HttpRequest,question_id:int):
     question= Question.objects.get(pk=question_id)
     question.delete()
     return redirect('main:home_view')

def update_view(request:HttpRequest,question_id:int):
        question = Question.objects.get(pk=question_id)
        if request.method == "POST":
            question.question= request.POST["question"]
            question.save()
            return redirect("quiz:all_question_view")

        return render(request, "quiz/update_question.html", {"question":question, "AnswerChoices": Question.AnswerChoices.choices})



def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})


