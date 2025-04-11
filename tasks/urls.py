from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.home, name='home'),                    # домашня сторінка
    path('tags/', views.tag_list, name='tag_list'),       # список тегів
    path('tasks/add/', views.add_task, name='add_task'),  # додавання задачі
    path('tags/add/', views.add_tag, name='add_tag'),     # додавання тегу
]
