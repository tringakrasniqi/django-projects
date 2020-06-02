from django.urls import path, include

urlpatterns = [
    path('', include('apps.books_authors.urls'))
]
