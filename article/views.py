from django.shortcuts import render

from .forms import ArticleForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def add_article(request):

    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }

    return render(request, 'add-article.html', context)
