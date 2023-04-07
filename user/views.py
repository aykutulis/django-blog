from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import RegisterForm


def register_user(request):

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User.objects.create_user(
                username=username, password=password)

            login(request, newUser)

            return redirect('index')

        return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'form': form})


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    return render(request, 'logout.html')
