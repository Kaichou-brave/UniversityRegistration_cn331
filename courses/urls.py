from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('courses', views.courses, name='courses'),
    path('course/<str:pk>', views.course, name='course'),
    path("book/<str:key>", views.book, name="book"),
    path("cancel/<str:key>", views.cancel, name="cancel"),
]
