from django.shortcuts import render
from .models import Project, Tutor

import django.http

# Create your views here.
def home(request):
    context = dict()
    context['title'] = 'Home'
    # query the projects tagged as special mention to show in home page
    context['highlighted'] = Project.objects.filter(special_mention=1)

    # query all the tutors to show as filters
    context['tutors'] = Tutor.objects.all()
    print(context['highlighted'])
    print(context['tutors'])

    # TO DO: render home template    
    return django.http.HttpResponse(content=str(context))