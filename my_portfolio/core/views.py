from django.shortcuts import render
from .models import About


def about(request ):
    about = About.objects.all()
    context = {
        'about': about,
    }
    # Render the 'about.html' template with the context data    

    return render(request, 'home.html' , context)