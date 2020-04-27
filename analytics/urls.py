from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='analytics'),
    path('analytics/', views.article_index, name='analytics_index'),
    re_path('analytics/(?P<slug>[\w-]+)', views.article_detail, name='article_detail'),
]
