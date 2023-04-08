from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm


def register_user(request):

    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newUser = User.objects.create_user(
            username=username, password=password)

        login(request, newUser)

        messages.success(request, 'Successfully registered.')
        return redirect('index')
    return render(request, 'register.html', context)


def login_user(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'User does not exist.')
            return render(request, 'login.html', context)

        login(request, user)
        messages.success(request, 'Successfully logged in.')
        return redirect('index')
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('index')
