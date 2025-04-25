from django.shortcuts import render

# Create your views here.
from .models import About

def home(request):
    about = About.objects.first()
  
    return render(request, 'home.html', {'about': about})
