from django.contrib import admin
from student.models import Student, Skill
from django.contrib.auth.models import User

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fields = ['user','year_in_school','school','skills']
    list_display = ['__unicode__','user','get_email','first_name','last_name','date_joined','school']

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = 'Mark selected skills as approved'

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_text','approved')
    actions = [approve]

admin.site.register(Student, StudentAdmin)
admin.site.register(Skill, SkillAdmin)
