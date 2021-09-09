from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Course


def registration(request):
    context = {'course': Course.objects.all(), 'enroll': Course.objects.filter(register=request.user)}
    return render(request, 'courses/registration-page.html', context)


def courses(request):
    context = {'course': Course.objects.all()}
    return render(request, 'courses/available-course.html', context)


def course(request, pk):
    courseObj = Course.objects.get(c_id=pk)
    return render(request, 'courses/single-course-info.html', {'course': courseObj})


def book(request, key):
    course = Course.objects.get(c_id=key)
    if request.user not in course.register.all():
        course.register.add(request.user)
        course.sit_count = course.register.count()
        if course.sit_count == course.max_sit:
            course.status = False
        course.save()
    return HttpResponseRedirect(reverse('registration'))


def cancel(request, key):
    course = Course.objects.get(c_id=key)
    if request.user not in course.register.all():
        messages.warning(request, "You are not enroll in this course yet")
    if request.user in course.register.all():
        messages.success(request, "Course Canceled")
        course.register.remove(request.user)
        course.sit_count = course.register.count()
        if course.sit_count != course.max_sit:
            course.status = True
        course.save()
    return HttpResponseRedirect(reverse("registration"))
