from django.urls import path, include

urlpatterns = [
    path('', include('apps.login_registration.urls')),
]
