from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('courses', views.courses, name='courses'),
    path('course/<str:pk>', views.course, name='course'),
    path("book/<str:key>", views.book, name="book"),

]
