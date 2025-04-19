from django.urls import path
from . import views


urlpatterns = [
    # Task routes
    path('', views.HomeView.as_view(), name='home'),
    path('task/add/', views.TaskCreateView.as_view(), name='task_add'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:task_id>/toggle/', views.ToggleTaskStatusView.as_view(), name='task_toggle'),

    # Tag routes
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/add/', views.TagCreateView.as_view(), name='tag_add'),
    path('tags/<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag_edit'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
]
