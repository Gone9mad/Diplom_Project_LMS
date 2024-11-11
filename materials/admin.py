from django.contrib import admin
from materials.models import Courses, Lesson


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name_courses', 'description', 'owner']
    search_fields = ['pk', 'name_courses']
    filter_fields = ['owner']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'courses', 'name_lesson', 'description', 'owner']
    search_fields = ['pk', 'name_lesson']
    filter_fields = ['owner', 'courses']
