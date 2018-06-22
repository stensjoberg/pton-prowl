from django.contrib import admin
from .models import Course, Code, Group
from students.models import Student
# Register your models here.

class CodeInline(admin.TabularInline):
    model = Code
    extra = 0
    readonly_fields = ['code',]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['students',]
    fieldsets = [
        ('Course Info',     {'fields': ['title','students']}),
    ]

    inlines = [CodeInline,]
    readonly_fields = ['id',]

class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Course Info',     {'fields': ['course','students']}),
    ]
    filter_horizontal = ['students']

    readonly_fields = ['course',]


admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)
