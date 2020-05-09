from django.shortcuts import render
from .models import Blog

def home(request):
    plists = Blog.objects 
    return render(request, 'home.html', {'plists' : plists})

