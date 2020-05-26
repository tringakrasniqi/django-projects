from django.urls import path, include

urlpatterns = [
    path('', include('apps.dojo_survey.urls')),
    path('random_word/', include('apps.random_word_generator.urls'))
]
