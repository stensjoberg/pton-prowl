from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from students.models import Student
from students.forms import AdminStudentChangeForm, AdminStudentCreationForm

class CourseEnrollmentInline(admin.TabularInline):
    model = Student.course_set.through

    verbose_name = "Course Enrollment"
    verbose_name_plural = verbose_name + "s"
    extra = 1

class GroupMembershipInline(admin.TabularInline):
    model = Student.group_set.through

    verbose_name = "Group Membership"
    verbose_name_plural = verbose_name + "s"
    extra = 1

class StudentAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = AdminStudentChangeForm
    add_form = AdminStudentCreationForm


    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('netid', 'email', 'full_name', 'class_year', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('netid', 'email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'class_year',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('netid', 'email', 'full_name', 'class_year', 'password1', 'password2')}
        ),
    )
    search_fields = ('netid',)
    ordering = ('netid',)
    filter_horizontal = ()
    inlines = (CourseEnrollmentInline, GroupMembershipInline,)

# Now register the new UserAdmin...
admin.site.register(Student, StudentAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
