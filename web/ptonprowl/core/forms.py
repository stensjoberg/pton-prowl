from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Course
from students.models import Student

class EnrollForm(forms.Form):
    course_id = forms.IntegerField(required=True)
    course_id.disabled = False

    def enroll(self):
        print(self.cleaned_data)
