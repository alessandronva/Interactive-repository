from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Project, Tutor
# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'tutor', 'special_mention')
    list_filter = ('date', 'tutor', 'special_mention')

admin.site.register(Tutor, TutorAdmin)
admin.site.register(Project, ProjectAdmin)

AdminSite.site_header = "Administracion Biblioteca UFT - Telecom"
AdminSite.site_title = "Biblioteca Telecom"