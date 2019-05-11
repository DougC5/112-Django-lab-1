from django.shortcuts import render
from django.http import HttpResponse


from .models import Movie, Genre

def index (request):
    catalog = Movie.objects.all() # read all the table
    # Movie.objects.filter(release_year = 2004)
    # Movie.objects.get(id=1)
    
    return render(request, 'views/index.html', {'catalog': catalog})

def test (request):
    return HttpResponse('<h1>I Am a Test</h1>')

def contact (request):
    return HttpResponse('<h1>I Am a Contact Page</h1>')