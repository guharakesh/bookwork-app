from django.contrib import admin
from student.models import Student, Skill

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fields = ['user','year_in_school','school','skills']

admin.site.register(Student, StudentAdmin)
admin.site.register(Skill)
