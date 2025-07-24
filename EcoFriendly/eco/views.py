from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Action, Comment
from .forms import ActionForm
from django.db.models import Count
import json
from django.db.models import Q

# Create your views here.

def new_action_view(request:HttpRequest):
     action_form = ActionForm()
     if request.method == "POST":
        action_form = ActionForm(request.POST, request.FILES)
        if action_form.is_valid():
            action_form.save()
            return redirect('main:home_view')
        else:
            print("not valid form")
            print(action_form.errors)
     return render(request, "eco/add_action.html",{"action_form":action_form , "LocationChoices": Action.LocationChoices.choices})

def all_action_view(request):
    location = request.GET.get('location')
    actions = Action.objects.all()
    if location and location != 'all':
        actions = actions.filter(location=location)
    data = Action.objects.values('location').annotate(count=Count('location'))
    labels = [entry['location'] for entry in data]
    counts = [entry['count'] for entry in data]

    context = {
        'actions': actions,
        'labels': json.dumps(labels),
        'counts': json.dumps(counts),
        'LocationChoices': Action.LocationChoices.choices,
    }
    return render(request, 'eco/all_actions.html', context)


def detail_view(request:HttpRequest, action_id:int):
      action = Action.objects.get(pk=action_id)
      comments = Comment.objects.filter(action=action)
      return render(request, 'eco/detail.html', {
        "action": action,
        "comments": comments, 
        "RatingChoices": Comment.RatingChoices.choices
})

def add_comment_view(request:HttpRequest, action_id):
    if request.method == "POST": 
        action = Action.objects.get(pk=action_id)
        new_comment = Comment(action= action ,
                            content= request.POST["content"],rating=request.POST["rating"])
        new_comment.save()
    

    return redirect("eco:detail_view", action_id= action_id )

def update_view(request:HttpRequest, action_id:int):
    action = Action.objects.get(pk=action_id)
    if request.method == "POST":
        action.title= request.POST["name"]
        action.description = request.POST["description"]
        action.location = request.POST["location"]
        if "image" in request.FILES: action.image = request.FILES["image"]
        action.save()
        return redirect("eco:detail_view", action_id)

    return render(request, "eco/update_action.html", {"action":action, "locationChoices": action.LocationChoices.choices})


def delete_view(request:HttpRequest, action_id:int):
     action= Action.objects.get(pk=action_id)
     action.delete()
     return redirect('main:home_view')

def search_view(request:HttpRequest):
    query = request.GET.get("search", "")
    action = []
    if query:
         action= Action.objects.filter(
    Q(title__icontains=query) | Q(location__icontains=query)
)
    return render(request, "eco/search.html", {"action": action})

