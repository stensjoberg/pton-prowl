# django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.template import Context
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect

# project imports
from .models import Course, Group
from .forms import EnrollForm

class IndexView(generic.ListView):
    template_name = 'core/index.html'
    form_class = EnrollForm

    form = EnrollForm()

    context = Context({
        'form': EnrollForm(),
    })

    def get_queryset(self):
        return Course.objects.order_by('-title')

class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form = EnrollForm
    context = Context({
        'form_class': EnrollForm,
        'form': EnrollForm,
    })

    model = Course
    template_name = 'core/detail.html'

class EnrollView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    template_name = 'core/enroll.html'
    success_url=''
    form_class = EnrollForm

    def form_valid(self, form):

        form.enroll()

        return super().form_valid(form)

"""# enrolls student in course
def enroll(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except (KeyError, Course.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'core/index.html', {
            'course': course,
            'error_message': "You didn't select a course.",
        })
    else:
        course.add_student(request.user)

        # creates new group for this user
        group = Group()
        group.set_course(course)
        group.add_student(request.user)


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('core:index'))

# de-enrolls students from course
def deroll(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except (KeyError, Course.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'core/index.html', {
            'course': course,
            'error_message': "You didn't select a course.",
        })
    else:

        groups = Group.objects.get(course=course)
        for group in groups:
            group.remove_student(request.user)

        course.remove_student(request.user)

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('core:index'))

# merges two groups, transfering students
def merge_groups(request, gone_id, gtwo_id):
    return
    """
