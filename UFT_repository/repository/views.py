from django.shortcuts import render
from .models import Project, Tutor
from UFT_repository import settings

import datetime
import django.http


def get_search_years():
    query = Project.objects.all().order_by('date')
    min, max = query.first().date.year, query.last().date.year

    print("AÑOS -->", min, max)

    return [str(year) for year in range(min, max + 1)]

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
    context['projects'] = list(enumerate(Project.objects.filter(special_mention=1).order_by('date').reverse(), 1))[:10]

    # query all the tutors to show as filters
    context['tutors'] = Tutor.objects.all()
    print(context['projects'])
    print(context['tutors'])

    return render(request, "home.html", context)

def search(request, page : int):
    context = dict()
    context['style_table'] = True
    context['style_search'] = True
    context['years'] = get_search_years()
    context['tutors'] = Tutor.objects.all()

    form_data = dict(request.GET) # dict

    # form data values are a list containing a str with the form value
    # take the value as a str and not a list
    for key in form_data:
        form_data[key] = form_data[key][0]

    # "spec_mention" appears on the request if selected with the value of "on"
    # take "on" as True, if it doesnt appears it wasn't checked, take as False
    if "spec_mention" in form_data:
        form_data["spec_mention"] = True
    else:
        form_data["spec_mention"] = False

    context['title'] = form_data['title']

    # Query database and filter by the title with a NO CASE SENSITIVE SEARCH
    # if no title was searched get all the projects
    if not form_data['title']:
        query = Project.objects.all().order_by('date').reverse()
    else:
        query = Project.objects.filter(title__icontains=form_data['title']).order_by('date').reverse()

    # if a tutor was selected get the projects associated with the given tutor
    if form_data['tutor']:
        query = query.filter(tutor__name__exact = form_data['tutor'])

    # get the projects between "year_low" and "year_high"
    query = query.filter(
        date__gte= datetime.date(int(form_data['year_low']), 1, 1),
        date__lte= datetime.date(int(form_data['year_high']), 12, 31)
    )

    # Remove special-mentions projects if the option was unchecked 
    if not form_data['spec_mention']:
        query = query.filter(special_mention = False)

    # get how many projects returns the query
    length = len(query)
    context['search_length'] = length

    pages_amount = int(length / 10) + 1

    print(f"\n\nProjects-->{length}\nPages--> {pages_amount}")
    context['active_page'] = page
    context['last_page'] = pages_amount - 1

    context['query_str'] = str(request.META['QUERY_STRING'])

    # calculate necesaries pages
    PROJECTS_PER_PAGE = 10
    PAGE_RANGE = (page-1)*PROJECTS_PER_PAGE

    context['page_buttons'] = list()
    if page < 3 and pages_amount > 3:
        context['page_buttons'] = [index for index in range(1,5)]
        context['show_last_page'] = True

    elif pages_amount > 3 and page < pages_amount-2:
        context['page_buttons'] = [index for index in range(page - 2, page + 2)]
        context['show_last_page'] = True
        if page - 2 > 1:
            context['show_first_page'] = True
    
    elif pages_amount > 3 and not page < pages_amount-2:
        context['page_buttons'] = [index for index in range(page-2, pages_amount)]
        context['show_first_page'] = True

    else:
        context['page_buttons'] = [index for index in range(1, pages_amount + 1)]

    # aplit the query depending on the page
    print("\n\nPAGE-->",page)
    print("RANGE-->", PAGE_RANGE, PAGE_RANGE + PROJECTS_PER_PAGE)
    query = query[PAGE_RANGE: PAGE_RANGE + PROJECTS_PER_PAGE]

    print("\n\nBUSQUEDA\n\n", query)
    if page == 1:
       context['projects'] = list(enumerate(query, 1))
    else:
        context['projects'] = list(enumerate(query, PAGE_RANGE + 1))

    # add to context the title 
    context['title'] = f"Buscar {form_data['title']}"

    # add the form searched values to render the form with then
    context['form'] = form_data
    print(form_data)

    print("\n\nREQUEST-->", str(request.path_info))
    print("\n PRUEBA-->", str(request.path_info) + "?" + str(request.META['QUERY_STRING']))

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

    file = f"{base_dir}/media/{filename}"
    print("FILE-->", file)
    response = django.http.HttpResponse(open(file, 'rb').read(), content_type='application/pdf')

    try:
        filename = str(filename).replace('files/', "")
        print("NEW FILENAME-->", filename)
    except Exception as error:
        print("ERROR-->", error)

    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response