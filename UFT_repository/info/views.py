from django.shortcuts import render
from django.http import HttpResponse

from UFT_repository.settings import BASE_DIR

from .models import Employee

# Create your views here.
def about(request):
    context = dict()
    context['title'] = 'Sobre nosotros'
    context['style_about'] = True

    context["query"] = Employee.objects.all()
    #img = query.img.url

    return render(request, template_name='about.html', context=context)