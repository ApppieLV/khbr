from .models import Links

def links(request):
    links = Links.objects.all()
    return {'links': links}