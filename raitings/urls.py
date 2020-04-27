from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='raitings'),
    re_path('(?P<slug>[\w-]+)', raiting_detail, name='raiting_detail'),
]