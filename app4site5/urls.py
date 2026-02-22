from django.urls import path

from app4site5 import views

urlpatterns = [
    path('', views.index),
]