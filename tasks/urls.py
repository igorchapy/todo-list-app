from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),                    # Using HomeView class
    path('tags/', views.TagListView.as_view(), name='tag_list'),         # Using TagListView class
    path('tasks/add/', views.TaskCreateView.as_view(), name='add_task'),  # Using TaskCreateView class
    path('tags/add/', views.TagCreateView.as_view(), name='add_tag'),     # Using TagCreateView class
]
