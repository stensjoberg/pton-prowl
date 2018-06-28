from django.contrib import admin
from .models import Course, Code, Group
from users.models import User
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
    fieldsets = [
        ('Course Info',     {'fields': ['title','users']}),
    ]

    filter_horizontal = ['users',]

    #inlines = [CodeInline,]

class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Course Info',     {'fields': ['course','users']}),
    ]
    filter_horizontal = ['users']

    readonly_fields = []


admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)
