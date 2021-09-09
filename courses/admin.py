from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ("c_id", "title", "semester", "year", "sit_count", "max_sit", "status")
    filter_horizontal = ("register",)

admin.site.register(Course, CourseAdmin)
