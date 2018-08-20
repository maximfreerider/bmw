from django.urls import path, include
from django.contrib import admin
from cars import views


urlpatterns = [
    path(r'bmw/', views.cars, name='cars'),
]