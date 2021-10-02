from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .models import Course


class CourseTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        password1 = make_password('somepass@brave')
        password2 = make_password('somepass@jj')

        user1 = User.objects.create(username='brave', password=password1)
        user2 = User.objects.create(username='jj', password=password2)

        Course.objects.create(c_id="test1")
        Course.objects.create(c_id="test2", max_sit=1)

    def test_str_is_equal_to_c_id(self):
        course = Course.objects.get(c_id='test1')

        self.assertEqual(str(course), course.c_id)

    def test_registration_view(self):
        self.client.login(username='jj', password='somepass@jj')

        response = self.client.get(reverse('courses:registration'))
        self.assertEqual(response.status_code, 200)

    def test_registration_view_context(self):
        self.client.login(username='jj', password='somepass@jj')

        response = self.client.get(reverse('courses:registration'))
        self.assertEqual(response.context['course'].count(), Course.objects.count())

    def test_guest_need_login_access_registration_page(self):
        response = self.client.get(reverse('courses:registration'))
        self.assertEqual(response.status_code, 302)

    def test_courses_view(self):
        self.client.login(username='brave', password='somepass@brave')

        response = self.client.get(reverse('courses:courses'))
        self.assertEqual(response.status_code, 200)

    def test_courses_view_context(self):
        self.client.login(username='brave', password='somepass@brave')

        response = self.client.get(reverse('courses:courses'))
        self.assertEqual(response.context['course'].count(), Course.objects.count())

    def test_course_view(self):
        self.client.login(username='jj', password='somepass@jj')

        course = Course.objects.first()
        response = self.client.get(reverse('courses:course', args=(course.c_id,)))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_book_course(self):
        self.client.login(username='jj', password='somepass@jj')

        course = Course.objects.first()
        response = self.client.get(reverse('courses:book', args=(course.c_id,)))
        self.assertEqual(course.register.first(), User.objects.get(username='jj'))

    def test_close_course_in_book_when_full(self):
        self.client.login(username='brave', password='somepass@brave')

        course = Course.objects.get(c_id='test2')
        response = self.client.get(reverse('courses:book', args=(course.c_id,)))
        course.refresh_from_db()
        self.assertEqual(course.status, False)

    def test_guest_cannot_book_course(self):
        course = Course.objects.first()
        response = self.client.get(reverse('courses:book', args=(course.c_id,)))
        self.assertEqual(response.status_code, 302)

    def test_redirect_book_course(self):
        self.client.login(username='brave', password='somepass@brave')

        course = Course.objects.first()
        response = self.client.get(reverse('courses:book', args=(course.c_id,)))
        self.assertRedirects(response, reverse('courses:registration'))

    def test_authenticated_user_can_cancel_course(self):
        self.client.login(username='jj', password='somepass@jj')

        course = Course.objects.first()
        course.register.add(User.objects.get(username='jj'))
        response = self.client.get(reverse('courses:cancel', args=(course.c_id,)))
        self.assertEqual(course.register.count(), 0)

    def test_guest_cannot_cancel_course(self):
        course = Course.objects.first()
        response = self.client.get(reverse('courses:cancel', args=(course.c_id,)))
        self.assertEqual(response.status_code, 302)

    def test_redirect_cancel_course(self):
        self.client.login(username='jj', password='somepass@jj')

        course = Course.objects.first()
        response = self.client.get(reverse('courses:cancel', args=(course.c_id,)))
        self.assertRedirects(response, reverse('courses:registration'))
