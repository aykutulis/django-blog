from django.contrib import admin
from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-article/', views.add_article, name='add-article'),
    path('article/<int:id>', views.detail, name='detail'),
    path('edit/<int:id>', views.update_article, name='update-article'),
    path('delete/<int:id>', views.delete_article, name='delete-article'),
    path('', views.articles, name='articles'),
]
