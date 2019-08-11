from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


#from django.http import HttpResponse

from .forms import LoginForm, UserRegisterForm
# Create your views here.
def user_login(request):
    context = {}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                # messages.success(request, f'Welcome: {user.username}')
                return redirect('todo-home')
            else:
                messages.error(request, 'Incorrect Username or Password')

    form = LoginForm
    context.update(form=form)
    return render(request, 'accounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('todo-home')

def user_register(request):
    context = {}

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data['password']
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('todo-home')
        else:
            return render(request, 'accounts/register.html', {'form':form})
    else:
        form = UserRegisterForm()
        context.update(form=form)
    return render(request, 'accounts/register.html', context)
