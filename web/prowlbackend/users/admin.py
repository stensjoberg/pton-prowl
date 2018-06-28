from django.contrib import admin
from django.contrib.auth.models import Group as AuthGroup
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User

from users.forms import AdminUserChangeForm, AdminUserCreateForm

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = AdminUserChangeForm
    add_form = AdminUserCreateForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('netid', 'email', 'full_name', 'class_year', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('netid', 'email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'class_year',)}),
        ('Permissions', {'fields': ('is_superuser',)}),
        ('Enrolled Courses', {'fields': ('courses',)}),
        ('Group Memberships', {'fields': ('groups',)}),
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
    filter_horizontal = []

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(AuthGroup)
