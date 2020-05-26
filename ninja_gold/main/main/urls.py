from django.urls import path, include

urlpatterns = [
    path('', include('apps.ninja_gold.urls')),
]
