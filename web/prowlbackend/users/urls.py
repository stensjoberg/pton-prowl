from django.urls import include, path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<str:pk>', views.UserDetailView.as_view(), name='user-detail')
]
