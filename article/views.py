from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Article
from .forms import ArticleForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'dashboard.html', {'articles': articles})


def add_article(request):

    form = ArticleForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, 'Successfully added article.')
        return redirect('article:dashboard')

    return render(request, 'add-article.html', context)


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'detail.html', {'article': article})
