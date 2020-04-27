from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def main(request):
    list_rait = Raiting.objects.filter(is_active=True).order_by('-created')    
    context = {'list_rait': list_rait}
    return render(request, 'raitings/index.html', context)

    
def raiting_detail(request, slug):
    data_rait = get_object_or_404(Raiting, slug=slug)
    data_rait.views += 1
    data_rait.save()
    return render(request, 'raitings/raiting_detail.html', locals())