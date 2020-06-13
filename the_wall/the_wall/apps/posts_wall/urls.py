from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('message/new', views.new_message),
    path('message/<int:message_id>/comment', views.new_comment),
    path('message/<int:message_id>/delete', views.delete_message)
]
