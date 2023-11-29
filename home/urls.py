from django.urls import path, include
from .views import mentorview, indexview, aboutview, coursesview, contactview
urlpatterns = [
    path('', indexview, name='home'),
    path('trainers/', mentorview, name='mentor'),
    path('about-team/', aboutview, name='about_team'),
    path('courses/', coursesview, name='courses'),
    path('contact_us/', contactview, name='contact')
]
