from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from raitings.models import Raiting
from event.models import Event
from videooverview.models import VideoDownloading
from .forms import SubscribeForm

def main(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('analytics')
        else:
            return redirect('analytics')
    else:
        form = SubscribeForm()
        last_art = Article.objects.filter(is_active=True).order_by('-created')[0:5]
        data_rait = Raiting.objects.filter(is_active=True).order_by('-created')[0:3]
        data_art_1_4 = Article.objects.filter(is_active=True)[0:3]
        data_video = VideoDownloading.objects.filter(is_active=True)[0:5]
        data_art_6_9 = Article.objects.filter(is_active=True)[5:8]
        data_event = Event.objects.filter(is_active=True)[0:3]
        integer_day = Article.objects.filter(integer_of_day=True).last()
    return render(request, 'analytics/index.html', locals())

def article_index(request):
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    return render(request, 'analytics/article_index.html', locals())

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()
    return render(request, 'analytics/article_detail.html', locals())

def not_found_view(request, exception):
    return render(request, 'errors/404.html')

def error_view(request):
    return render(request, 'errors/500.html')

def permission_denied_view(request, exception):
    return render(request, 'errors/403.html')

def bad_request_view(request, exception):
    return render(request, 'errors/400.html')