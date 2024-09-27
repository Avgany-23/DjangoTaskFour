import school.management.commands.django_settings
from website import settings
from school.models import Student, Teacher, StudentsTeachers
import json

def start_migrate():
    with open(settings.BASE_DIR / 'school.json', encoding='utf-8') as f:
        reader = json.load(f)
        s, t = [], []
        def mmm():
            for person in reader:
                if person['model'].endswith('teacher'):
                    t.append(Teacher(name=person['fields']['name'], subject=person['fields']['subject']))
                    continue
                s.append(Student(name=person['fields']['name'], group=person['fields']['group']))

        for i in range(1000):
            mmm()

        Student.objects.bulk_create(s)
        Teacher.objects.bulk_create(t)
        print(f"Таблица Student и Teacher заполнены")

def migrate_many_to_many():
    student = Student.objects.all()
    stud_teach = []
    for s in student:
        teachers = Teacher.objects.filter(id=s.id)
        for t in teachers:
            stud_teach.append(StudentsTeachers(students_id=s.id, teachers_id=t.id))
    StudentsTeachers.objects.bulk_create(stud_teach)
    print(f"Таблица StudentsTeachers заполнена")