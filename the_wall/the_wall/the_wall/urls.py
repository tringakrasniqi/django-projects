from django.urls import path, include

urlpatterns = [
    path('', include('apps.authenticate.urls')),
    path('wall/', include('apps.posts_wall.urls'))
]
