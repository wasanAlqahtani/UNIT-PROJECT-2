from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Action, Comment
from .forms import ActionForm
from django.db.models import Count
import json
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Avg
from django.contrib import messages
# Create your views here.

def new_action_view(request:HttpRequest):
    '''This function is used to add new action its take request and return the action and location choices 
    when its added a messsage will display for user and redirent to detailed page '''
    if request.method == 'POST':
        # create object from action form 
        action_form = ActionForm(request.POST, request.FILES)
        if action_form.is_valid():
            action = action_form.save()
            #display message 
            messages.success(request, "Your Add Was Done Successfully.")
            return redirect("eco:detail_view",action.id)
    else:
        #empty 
        action_form = ActionForm()
   
    return render(request, "eco/add_action.html", {
        "action_form": action_form,
        "LocationChoices": Action.LocationChoices.choices
    })

def all_action_view(request:HttpRequest):
    '''This function show all the actions and display chart based on location and also 
    have filter by location the function take the request and return all the actions 
    and when the user filter in specific location it will display all actions related
    to the location. As well as, divaded the actions into pages (every 3 in one page )'''
    #take the location filter 
    location = request.GET.get('location')
    #all actions with rating 
    actions = Action.objects.all().annotate(avg_rating=Avg('comment__rating'))
    if location and location != 'all':
        #filter 
        actions = actions.filter(location=location)
    #Paginator to divide the actions into pages 
    paginator = Paginator(actions, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # for creating chart based on locations 
    data = Action.objects.values('location').annotate(count=Count('location'))
    labels = [entry['location'] for entry in data]
    counts = [entry['count'] for entry in data]

    context = {
        'page_obj': page_obj,
        'labels': json.dumps(labels),
        'counts': json.dumps(counts),
        'LocationChoices': Action.LocationChoices.choices,
        'selected_location': location or 'all',
    }
    return render(request, 'eco/all_actions.html', context)


def detail_view(request:HttpRequest, action_id:int):
      '''This function takes request and action id to diplay the detail of an action and also display and add comments '''
      #display the detailes of this action
      action = Action.objects.get(pk=action_id)
      #comment of this action 
      comments = Comment.objects.filter(action=action)
      return render(request, 'eco/detail.html', {
        "action": action,
        "comments": comments, 
        "RatingChoices": Comment.RatingChoices.choices
})

def add_comment_view(request:HttpRequest, action_id):
    '''This function for adding comment of specific action, its take the request and the id and then create comment and save it 
    and redirect to deatiled page '''
    if request.method == "POST": 
        #action on this is 
        action = Action.objects.get(pk=action_id)
        #create comment 
        new_comment = Comment(action= action ,
                            content= request.POST["content"],rating=request.POST["rating"])
        new_comment.save()
    

    return redirect("eco:detail_view", action_id= action_id )

def update_view(request:HttpRequest, action_id:int):
    '''This function Uppdated values of the action, its take request and id and then update the values
    after that a message will display to the user and redirect to detail page '''
    #action on this id 
    action = Action.objects.get(pk=action_id)
    if request.method == "POST":
        #update values 
        action.title= request.POST["title"]
        action.description = request.POST["description"]
        action.location = request.POST["location"]
        if "image" in request.FILES: action.image = request.FILES["image"]
        action.save()
        #send message 
        messages.success(request, "Your Update Was Done Successfully.")
        return redirect("eco:detail_view", action_id)

    return render(request, "eco/update_action.html", {"action":action, "locationChoices": action.LocationChoices.choices})


def delete_view(request:HttpRequest, action_id:int):
     '''This function delete specific action its take a request and action is and then delete this action
     and redirect to home page '''
     action= Action.objects.get(pk=action_id)
     action.delete()
     return redirect('main:home_view')

def search_view(request:HttpRequest):
    '''this function search based on text or location, its take requuest and then search for action
    depend on the search and then redirect to search page '''
    #quesry for search result 
    query = request.GET.get("search", "")
    action = []
    if query:
         # actions based on the search 
         action= Action.objects.filter(
    Q(title__icontains=query) | Q(location__icontains=query)
    ).annotate(avg_rating=Avg('comment__rating'))
    return render(request, "eco/search.html", {"action": action})

