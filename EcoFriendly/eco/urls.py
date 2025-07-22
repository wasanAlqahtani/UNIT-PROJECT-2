from django.urls import path
from . import views
app_name = "eco"
urlpatterns = [
    path("new/",views.new_action_view, name="new_action_view"),
    path("all/", views.all_action_view, name="all_action_view"),
    path("<action_id>/detail/", views.detail_view, name="detail_view"),
    path("<action_id>/update/", views.update_view, name="update_view"),
    path("<action_id>/delete/",views.delete_view, name="delete_view"),
]