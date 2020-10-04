from django.shortcuts import render
from django.http import HttpResponse

from UFT_repository.settings import BASE_DIR

from .models import Employee, Contact

# Create your views here.
def about(request):
    context = dict()
    context['title'] = 'Sobre nosotros'
    context['style_about'] = True

    query = Employee.objects.all().filter(status=True)

    context['bosses'] = query.filter(role='boss')
    context['teachers'] = query.filter(role='prof')
    context['admins'] = query.filter(role='admin')

    context['contacts'] = Contact.objects.all()

    context['show_devs'] = True

    return render(request, template_name='about.html', context=context)