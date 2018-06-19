# django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# project imports
from .models import Student

def index(request):
    return HttpResponse("Hello, world!")

class AccountDetails( LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
    model = Student
    template_name = 'students/account.html'

    # delivers user object upon request
    def get_object(self):
            return get_object_or_404(Student, netid=self.kwargs.get('netid'))
