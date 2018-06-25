from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:course_id>/add/', views.enroll, name='enroll'),
]
