from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('users', views.get_users),
    path('profile', views.get_user_profile),
]