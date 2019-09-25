from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('who/', views.who, name='who'),
    path('contact/', views.contact, name='contact'),
]
