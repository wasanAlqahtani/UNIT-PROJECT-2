from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Action, Comment
from .forms import ActionForm
from django.db.models import Count
import json

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
    actions = Action.objects.all()
    data = Action.objects.values('location').annotate(count=Count('location'))
    labels = [entry['location'] for entry in data]
    counts = [entry['count'] for entry in data]

    context = {
        'actions': actions,
        'labels': json.dumps(labels),
        'counts': json.dumps(counts),
    }
    return render(request, 'eco/all_actions.html', context)


def detail_view(request:HttpRequest, action_id:int):
      action = Action.objects.get(pk=action_id)
      same_location = Action.objects.filter(location=action.location).exclude(id=action.id)[0:3]
      comments = Comment.objects.filter(action=action)
      return render(request, 'eco/detail.html', {
        "action": action,
        "same_location": same_location,
        "comment" : comments, 
})

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
