from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('groups/', views.GroupListView.as_view(), name='groups'),
    path('codes/', views.CodeListView.as_view(), name='codes'),

    path('courses/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('groups/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),
    path('codes/<str:pk>', views.CodeDetailView.as_view(), name='code-detail')


]
