from django.urls import path
from . import views

app_name = "eco"
#urls in eco app 
urlpatterns = [
    path("new/",views.new_action_view, name="new_action_view"),
    path("all/", views.all_action_view, name="all_action_view"),
    path("<action_id>/detail/", views.detail_view, name="detail_view"),
    path("<action_id>/update/", views.update_view, name="update_view"),
    path("<action_id>/delete/",views.delete_view, name="delete_view"),
    path("comments/add/<action_id>", views.add_comment_view, name="add_comment_view"),
    path("search/", views.search_view, name="search_view"),
]