# django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

# project imports
from .models import Course

class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-title')

class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Course
    template_name = 'core/detail.html'

def add_course(request, id):
    course = get_object_or_404(Course, pk=id)
    course.add_student(user)

    return HttpResponseRedirect(reverse('core', args(course.id)))
