from django.urls import include, path

from . import views

app_name = 'users'
urlpatterns = [
    path('users', views.UserListView.as_view()),
    path('users/<str:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('validate', views.ValidateView.as_view(), name='validate')
]
