from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('register_user', views.register),
	path('login_user', views.login),
]