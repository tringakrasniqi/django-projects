from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses/create', views.create_course),
    path('courses/confirm_delete/<int:course_id>', views.confirm_delete),
    path('courses/delete/<int:course_id>', views.delete_course),
    path('courses/add_comment/<int:course_id>', views.add_comment),
    path('courses/create_comment/<int:course_id>', views.create_comment)
]
