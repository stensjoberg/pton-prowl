from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import User
from core.models import Course, Group

class AdminUserCreateForm(forms.ModelForm):
    """"A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('netid', 'full_name', 'class_year',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.availability = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AdminUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('netid', 'full_name', 'class_year', 'password', 'is_active', 'is_superuser')

    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Courses',
            is_stacked=False
        )
    )

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Groups',
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(AdminUserChangeForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['courses'].initial = self.instance.courses.all()
            self.fields['groups'].initial = self.instance.groups.all()


    def save(self, commit=True):
        User = super(AdminUserChangeForm, self).save(commit=False)
        if commit:
            User.save()

        if User.pk:
            User.courses.set(self.cleaned_data['courses'])
            User.groups.set(self.cleaned_data['groups'])
            print(self)
            self.save_m2m()

        return User

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
