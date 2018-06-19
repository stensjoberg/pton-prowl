# django imports
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

# project imports
from .models import Course

class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-title')[:5]

class DetailView(generic.DetailView):
    model = Course
    template_name = 'core/detail.html'
