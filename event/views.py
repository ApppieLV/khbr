from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def main(request):
    list_event = Event.objects.filter(is_active=True).order_by('-created')
    return render(request, 'event/index.html', locals())

def event_detail(request, slug):
    data_event = get_object_or_404(Event, slug=slug)
    data_event.views += 1
    data_event.save()
    return render(request, 'event/event_detail.html', locals())