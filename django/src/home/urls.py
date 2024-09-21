from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'home'


urlpatterns = [
    path('', views.views.HomeView.as_view(), name="home"),
    path('record/', views.views.RecordView.as_view(), name="record"),
    path('deside/', views.views.DesideView.as_view(), name="deside"),
    path('watch/', views.views.WatchView.as_view(), name="watch"),
      
]