from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Student

def index(request):
    return HttpResponse("Hello, world!")

class AccountDetails(generic.DetailView):
    model = Student
    template_name = 'students/account.html'

    def get_object(self):
            return get_object_or_404(Student, netid=self.kwargs.get('netid'))
