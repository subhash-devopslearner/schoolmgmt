from django.contrib import admin
from .models import AcademicYear, Department, AcademicTerm, AcademicClass, Student, Faculty, Subject
from import_export.admin import ImportExportModelAdmin
from .resources import StudentResource

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(Department)
admin.site.register(AcademicTerm)
admin.site.register(AcademicClass)
admin.site.register(Faculty)
admin.site.register(Subject)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_classes = [StudentResource]
    list_display = ('name', 'sap_id', 'roll_number', 'class_enrolled')
    search_fields = ('name', 'sap_id')
