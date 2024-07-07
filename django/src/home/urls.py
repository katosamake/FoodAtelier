from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'home'

urlpatterns = [
    path('', views.views.HomeView.as_view(), name="home")
]