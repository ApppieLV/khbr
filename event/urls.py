from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='events'),
    re_path('(?P<slug>[\w-]+)', views.event_detail, name='event_detail'),
]