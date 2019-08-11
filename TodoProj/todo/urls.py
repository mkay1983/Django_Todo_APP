from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='todo-home'),
    path('set_complete/<int:task_id>', views.set_complete, name="todo-set_complete"),
    path('add_todo/', views.add_todo, name='todo-add_todo'),
    path('delete_completed/', views.delete_completed, name="todo-delete_completed"),
    path('delete_all/', views.delete_all, name="todo-delete_all"),
]
