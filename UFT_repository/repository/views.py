from django.shortcuts import render
from .models import Project, Tutor
from UFT_repository import settings

import datetime
import django.http


def get_search_years():
    query = Project.objects.all().order_by('date')
    min, max = query.first().date.year, query.last().date.year

    print("AÑOS -->", min, max)

    return [year for year in range(min, max + 1)]

def get_tutors():
    return Tutor.objects.all() 

# Create your views here.
def home(request):
    context = dict()
    context['title'] = 'Inicio'
    context['style_table'] = True
    context['years'] = get_search_years()
    context['tutors'] = Tutor.objects.all()

    # query the projects tagged as special mention to show in home page
    context['projects'] = list(enumerate(Project.objects.filter(special_mention=1), 1))[:10]

    context['media'] = settings.MEDIA_ROOT + '/'

    # query all the tutors to show as filters
    context['tutors'] = Tutor.objects.all()
    print(context['projects'])
    print(context['tutors'])

    return render(request, "home.html", context)

def search(request):
    context = dict()
    context['style_table'] = True
    context['in_search'] = True
    context['years'] = get_search_years()
    context['tutors'] = Tutor.objects.all()

    form_data = dict(request.GET) # dict
    print(form_data)

    # form data values are a list containing a str with the form value
    # take the value as a str and not a list
    for key in form_data:
        form_data[key] = form_data[key][0]

    # "spec-mention" appears on the request if selected with the value of "on"
    # take "on" as True, if it doesnt appears it wasn't checked, take as False
    if "spec-mention" in form_data:
        form_data["spec-mention"] = True
    else:
        form_data["spec-mention"] = False

    context['title'] = form_data['title']

    # Query database and filter by the title with a NO CASE SENSITIVE SEARCH
    # if no title was searched get all the projects
    if not form_data['title']:
        query = Project.objects.all()
    else:
        query = Project.objects.filter(title__icontains=form_data['title'])

    # if a tutor was selected get the projects associated with the given tutor
    if form_data['tutor']:
        query = query.filter(tutor__name__exact = form_data['tutor'])

    # get the projects between "year-low" and "year-high"
    query = query.filter(
        date__gte= datetime.date(int(form_data['year-low']), 1, 1),
        date__lte= datetime.date(int(form_data['year-high']), 12, 31)
    )

    # Remove special-mentions projects if the option was unchecked 
    if not form_data['spec-mention']:
        query = query.filter(special_mention = False)

    print("\n\nBUSQUEDA\n\n", query)
    context['projects'] = list(enumerate(query, 1))

    return render(request, "home.html", context)
    #return django.http.HttpResponse(query)

def show_project(request, title):
    context = dict()
    context['title'] = 'Ver proyecto'
    context['style_description'] = True
    context['years'] = get_search_years()
    context['tutors'] = Tutor.objects.all()

    query = Project.objects.get(title=title)

    context['title'] = title
    context['description'] = query.description
    context['author'] = query.author
    context['date'] = query.date
    context['tutor'] = query.tutor
    context['special_mention'] = query.special_mention
    context['file'] = query.file.name

    print(context['file'])
    
    return render(request, "description.html", context)
    #return django.http.HttpResponse(query)


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