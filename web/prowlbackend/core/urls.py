from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('courses/', views.CourseListView.as_view()),
    path('groups/', views.GroupListView.as_view())
]
