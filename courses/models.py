from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    c_id = models.CharField(max_length=5, unique=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    semester = models.IntegerField()
    year = models.IntegerField()
    sit_count = models.IntegerField(default=0, null=True, blank=True)
    max_sit = models.IntegerField()
    status = models.BooleanField(default=True)
    register = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.c_id}"

