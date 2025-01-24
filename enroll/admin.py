from django.contrib import admin
from enroll.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'password')

# admin.site.register(Student , StudentAdmin )
