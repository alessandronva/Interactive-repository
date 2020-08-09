from django.shortcuts import render
from .models import Project, Tutor
from UFT_repository import settings

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

def show_project(request, title):
    context = dict()
    context['title'] = 'Ver proyecto'
    query = Project.objects.get(title=title)

    context['title'] = title
    context['description'] = query.description
    context['autor'] = query.autor
    context['date'] = query.date
    context['tutor'] = query.tutor
    context['special_mention'] = query.special_mention
    context['file'] = query.file
    
    # TO DO: render template
    return django.http.HttpResponse(query)


def download(request, filename):
    print("BASE DIR -->", settings.BASE_DIR)
    base_dir = settings.BASE_DIR
    base_dir = base_dir.replace("\\","/")
    filename = Project.objects.get(title=filename).file
    print("FILENAME-->", filename)

    file = f"{base_dir}/{ filename }"
    print("FILE-->", file)
    response = django.http.HttpResponse(open(file, 'rb').read(), content_type='application/pdf')

    try:
        filename = str(filename).replace('files/', "")
        print("NEW FILENAME-->", filename)
    except Exception as error:
        print("ERROR-->", error)

    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response