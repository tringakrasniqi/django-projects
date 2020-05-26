from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generate/', views.generate),
    path('reset/', views.reset)
]
