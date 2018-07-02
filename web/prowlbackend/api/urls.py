from django.urls import include, path
from django_cas_ng import views as cas_views

urlpatterns = [
    path('users/', include('users.urls')),
    path('', include('core.urls')),

    # CAS paths
    path('cas/login/', cas_views.login, name='login'),
    path('cas/logout/', cas_views.logout, name='logout'),

    # Rest auth
    path('rest-auth/', include('rest_auth.urls')),

    ]
