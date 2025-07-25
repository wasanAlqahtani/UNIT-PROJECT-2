from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
     path('', views.quiz_view, name="quiz_view"),
     path('add_question/', views.add_question_view, name='add_question_view'),
     path("all/", views.all_question_view, name="all_question_view"),
     path("<question_id>/delete/",views.delete_view, name="delete_view"),
     path("<question_id>/update/", views.update_view, name="update_view"),
]