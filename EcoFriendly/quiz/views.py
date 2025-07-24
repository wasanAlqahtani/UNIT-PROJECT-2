from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def quiz_view(request:HttpRequest):
     if 'question_num' not in request.session:
        request.session['question_num'] = 0
        request.session['answers'] = []

     question_num = request.session['question_num']
     questions = [
        "Do you save water at home?",
        "Do you use reusable bags?",
        "Do you avoid plastic products?",
        "Do you recycle regularly?",
        "Do you use public transportation?"
    ]

     if request.method == 'POST':
        answer = request.POST.get('answer')
        answers = request.session['answers']
        answers.append(int(answer))
        request.session['answers'] = answers

        question_num += 1
        request.session['question_num'] = question_num

        if question_num >= len(questions):
            score = sum(answers)
            del request.session['question_num']
            del request.session['answers']


            if score >=40 :
                result_type = ' 🥇 Eco Warrior'
            elif score >= 25 :
                result_type = ' 🍀 Eco Starter'  
            else :
                result_type = ' 🔴 Needs Improvement'
            return render(request, 'quiz/result.html', {'score': score, 'result_type': result_type})

     return render(request, 'quiz/quiz.html', {'question': questions[question_num], 'question_num': question_num})

