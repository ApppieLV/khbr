from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth

def signin(request):
    if request.method == 'POST':
        form = SignInUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('analytics')
            else:
                form = SignInUserForm()
        else:
            form = SignInUserForm()
    else:
        form = SignInUserForm()
    return render(request, 'user/signin.html', locals())

def signup(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.email = form.cleaned_data.get('email')
            user.username = form.cleaned_data.get('username')
            user.password = form.cleaned_data.get('password')
            form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')            
            return redirect('analytics')
        else:
            form = SignUpUserForm()
    else:
        form = SignUpUserForm()
    return render(request, 'user/signup.html', locals())