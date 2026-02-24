from django.contrib import admin
from .models import AcademicYear, Department, AcademicTerm, AcademicClass, Student, Faculty, Subject

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(Department)
admin.site.register(AcademicTerm)
admin.site.register(AcademicClass)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Subject)