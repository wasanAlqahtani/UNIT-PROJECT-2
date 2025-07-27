from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Avg
from eco.models import Action, Comment
from main.models import Contact
from django.contrib import messages
# Create your views here.


def home_view(request: HttpRequest):
    ''' this method take the request and return the latest action(3) with rating choices
      and redirect to home page  '''
    #action object (latest 3 ) and calculate the average review of each action 
    actions = Action.objects.annotate(avg_rating=Avg('comment__rating')).order_by('-created_at')[:3]

    # list that conatins reminder tips for user its change very few second 
    remainder_tips = [
        "Reduce Single-Use Plastics",
        "Conserve Energy",
        "Minimize Food Waste",
        "Choose Sustainable Transportation",
        "Opt for Eco-Friendly Products",
        "Embrace Reusables",
        "Support Local and Sustainable Brands",
        "Practice Water Conservation",
        "Go Paperless",
        "Educate and Inspire Others"
    ]

    return render(request, 'main/home.html', {
        "tips": remainder_tips,
        "actions": actions,
        "RatingChoices": Comment.RatingChoices.choices 
    })


def contact_view(request: HttpRequest):
    '''This method take request and save the contact form in message varible and 
    then return to contact page'''

    #save the inputs in object 
    if request.method == "POST":
        message = Contact(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            message=request.POST["message"]
        )
        #send message to the user that the message was sent success 
        message.save()
        messages.success(request, "Your message was sent successfully.")
        return redirect('main:contact_view')

    return render(request, "main/contact.html")


def messages_view(request:HttpRequest):
    '''This function take the request and return all the messages that from users and redirect to
    messages page '''

    # take all the messages from contact model 
    messages = Contact.objects.all()
    return render(request,"main/messages.html",{"messages": messages})

