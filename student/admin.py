from django.contrib import admin
from student.models import Student, Skill, Employer
from django.contrib.auth.models import User

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fields = ['user','year_in_school','school','skills','profile_pic']
    list_display = ['__unicode__','user','get_email','first_name','last_name','date_joined','school','profile_pic']

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = 'Mark selected skills as approved'

class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_text','approved']
    actions = [approve]

class EmployerAdmin(admin.ModelAdmin):
    fields = ['name','logo','description']
    list_display = ['__unicode__','name','logo','description']

admin.site.register(Student, StudentAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Employer, EmployerAdmin)
