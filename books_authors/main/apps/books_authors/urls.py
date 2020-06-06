from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_book', views.add_book),
    path('show_book/<int:book_id>', views.show_book),
    path('authors', views.show_authors),
    path('process_author', views.add_author),
    path('show_author/<int:author_id>', views.show_author)
]
