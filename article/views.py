from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .models import Article, Comment
from .forms import ArticleForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url='user:login')
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'dashboard.html', {'articles': articles})


@login_required(login_url='user:login')
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


@login_required(login_url='user:login')
def update_article(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, 'Successfully updated article.')
        return redirect('article:dashboard')

    return render(request, 'update-article.html', {'form': form})


@login_required(login_url='user:login')
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, 'Successfully deleted article.')
    return redirect('article:dashboard')


def articles(request):
    keyword = request.GET.get('keyword')
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, 'articles.html', {'articles': articles, 'keyword': keyword})
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})


@login_required(login_url='user:login')
def add_comment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        comment_content = request.POST.get('comment')

        if not comment_content:
            messages.warning(request, 'Comment cannot be empty.')
            return redirect(reverse('article:detail', kwargs={'id': id}))

        comment_author = request.user

        new_comment = Comment(comment_author=comment_author,
                              comment_content=comment_content)
        new_comment.article = article
        new_comment.save()

    return redirect(reverse('article:detail', kwargs={'id': id}))
