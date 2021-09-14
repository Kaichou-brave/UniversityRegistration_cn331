from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Course


@login_required(login_url='users:login')
def registration(request):
    context = {'course': Course.objects.all().order_by(
        'c_id'), 'enroll': Course.objects.filter(register=request.user)}
    return render(request, 'courses/registration-page.html', context)


@login_required(login_url='users:login')
def courses(request):
    context = {'course': Course.objects.all().order_by('c_id')}
    return render(request, 'courses/available-course.html', context)


def course(request, pk):
    courseObj = Course.objects.get(c_id=pk)
    return render(request, 'courses/single-course-info.html', {'course': courseObj})


@login_required(login_url='users:login')
def book(request, key):
    course = Course.objects.get(c_id=key)
    if request.user not in course.register.all():
        course.register.add(request.user)
        course.sit_count = course.register.count()
        if course.sit_count == course.max_sit:
            course.status = False
        course.save()
    return HttpResponseRedirect(reverse('registration'))


@login_required(login_url='users:login')
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
