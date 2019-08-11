from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskForm
from .models import Todo
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    context = {}
    todo_list = Todo.objects.filter(user=request.user.id)
    context.update(todos=todo_list)
    form = TaskForm()
    context.update(form=form)

    return render(request, 'todo/home.html', context)

def set_complete(request, task_id):

    comp = Todo.objects.get(pk=task_id)
    comp.complete = True
    comp.save()

    return redirect('todo-home')

def delete_completed(request):
    comp_todos = Todo.objects.filter(user=request.user.id).filter(complete=True)
    comp_todos.delete()

    return redirect('todo-home')

def delete_all(request):

    Todo.objects.filter(user=request.user.id).delete()
    return redirect('todo-home')

def add_todo(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            new_todo = Todo(task=form.cleaned_data['task'], state=request.POST.get('state'), user=request.user)
            new_todo.save()


    return redirect('todo-home')
