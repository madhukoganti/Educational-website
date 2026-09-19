from django.contrib import admin
from app1.models import Student, Contact


class StudentAdmin(admin.ModelAdmin):
    list_display = ['NAME', 'PHONE', 'EMAIL', 'SNAME', 'MSG']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['NAME', 'PHONE', 'EMAIL', 'MSG']


admin.site.register(Student, StudentAdmin)
admin.site.register(Contact, ContactAdmin)