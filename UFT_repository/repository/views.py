from django.shortcuts import render
from .models import Project, Tutor

import django.http

# Create your views here.
def home(request):
    context = dict()
    context['title'] = 'Home'
    context['highlighted'] = Project.objects.filter(special_mention=1)

    print(context['highlighted'])

    
    return django.http.HttpResponse(content=str(context))