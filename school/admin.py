from django.contrib import admin
from .models import Student, Teacher, StudentsTeachers


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentsTeachers)
class TeacherAdmin(admin.ModelAdmin):
    pass