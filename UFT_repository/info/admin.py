from django.contrib import admin
from .models import Employee, Contact

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'status')
    list_filter = ("role", "status")

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Contact, ContactAdmin)