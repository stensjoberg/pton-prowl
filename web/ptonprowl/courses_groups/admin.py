from django.contrib import admin
from .models import Course, CourseID, Group

# Register your models here.

admin.site.register(Course)
admin.site.register(CourseID)
admin.site.register(Group)
