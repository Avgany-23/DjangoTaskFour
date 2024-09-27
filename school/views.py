from django.views.generic import ListView
from .models import Student


class StudentsList(ListView):
    template_name = 'school/students_list.html'
    context_object_name = 'object_list'
    queryset = Student.objects.prefetch_related('teacher').all()
    # queryset = Student.objects.all()
    ordering = 'group'
