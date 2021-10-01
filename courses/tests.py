from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Course


class CourseTestCase(TestCase):

    def setUp(self):
        password1 = make_password('somepass@brave')
        password2 = make_password('sompass@jj')
        user1 = User.objects.create(username='brave', password=password1)
        user2 = User.objects.create(username='jj', password=password2)

        Course.objects.create(c_id="test")

    def test_str_is_equal_to_c_id(self):
        course = Course.objects.get(c_id='test')

        self.assertEqual(str(course), course.c_id)

