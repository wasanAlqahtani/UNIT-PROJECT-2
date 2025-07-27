import json
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Question
from .forms import QuestionForm
from django.contrib import messages

# Create your views here.
def all_question_view(request:HttpRequest):
    '''This function display all questions it takes request and return all questions '''
    #create question object to retun all question 
    questions = Question.objects.all()
    return render(request, 'quiz/all_questions.html', {"questions":questions})

def add_question_view(request:HttpRequest):
    '''This function add new question using questionform it takes request,
        and then return a message and redirect to all question view'''
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            #display message 
            messages.success(request, "Your Add Was Done Successfully.")
            return redirect('quiz:all_question_view') 
        
    return render(request, 'quiz/add_question.html', {'form': form ,"AnswerChoices": Question.AnswerChoices.choices})

def delete_view(request:HttpRequest,question_id:int):
     '''This function delete specific question it takes
      request and question id,  and then return to all question view '''
     #create question object with specific id and delete it
     question= Question.objects.get(pk=question_id)
     question.delete()
     return redirect('quiz:all_question_view')

def update_view(request:HttpRequest,question_id:int):
        '''This function update specific question it takes request and question id, and then
        update it and redirect to all question view '''
        question = Question.objects.get(pk=question_id)
        if request.method == "POST":
            question.question= request.POST["question"]
            question.save()
            messages.success(request, "Your Update Was Done Successfully.")
            return redirect("quiz:all_question_view")

        return render(request, "quiz/update_question.html", {"question":question, "AnswerChoices": Question.AnswerChoices.choices})

def quiz_view(request: HttpRequest):
    '''this function to create or start quiz it takes request and then take all question and send it
    to quiz.html page to diplay the  question to the user '''

    #create question object to get  all question 
    questions = Question.objects.all()
    #convert the model object to list inside it dictionary to let java script handle it using json 
    #to read it well and can handle it and display one question per page and count the total 
    questions_data = [
        {
            'id': q.id,
            'question': q.question,
            'choices': {
                'a': q.choice_a,
                'b': q.choice_b,
                'c': q.choice_c,
                'd': q.choice_d,
            },
            'correct': q.correct_choice.lower(),
            'explanation': q.explanation or "",
        }
        for q in questions
    ]

    return render(request, 'quiz/quiz.html', {
        'questions_json': json.dumps(questions_data),
    })





