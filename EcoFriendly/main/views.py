from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Avg
from eco.models import Action, Comment
from main.models import Contact
# Create your views here.
def home_view(request: HttpRequest):
    actions = Action.objects.annotate(avg_rating=Avg('comment__rating')).order_by('-created_at')[:3]

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

from django.contrib import messages

def contact_view(request: HttpRequest):
    if request.method == "POST":
        message = Contact(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            message=request.POST["message"]
        )
        message.save()
        messages.success(request, "Your message was sent successfully.")
        return redirect('main:contact_view')

    return render(request, "main/contact.html")


def messages_view(request:HttpRequest):
    messages = Contact.objects.all()
    return render(request,"main/messages.html",{"messages": messages})

