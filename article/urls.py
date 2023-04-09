from django.contrib import admin
from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-article/', views.add_article, name='add-article'),
    path('article/<int:id>', views.detail, name='detail'),
]
