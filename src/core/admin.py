from django.contrib import admin
from .models import AcademicYear, Department, AcademicTerm, AcademicClass, Student, Faculty, Subject

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(Department)
admin.site.register(AcademicTerm)
admin.site.register(AcademicClass)
#admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Subject)


class StudentResource(resources.ModelResource):
    # This matches "MBATech CE Sem-VI Div-A (2025-2026)" from Excel to your Class
    class_enrolled = fields.Field(
        column_name='class_name',
        attribute='class_enrolled',
        widget=ForeignKeyWidget(AcademicClass, 'class_name')
    )

    class Meta:
        model = Student
        # sap_id is used to identify the student (prevents duplicates)
        import_id_fields = ('sap_id',)
        # Only import these 4 fields
        fields = ('class_enrolled', 'sap_id', 'roll_number', 'name')

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_classes = [StudentResource]
    list_display = ('name', 'sap_id', 'roll_number', 'class_enrolled')
    search_fields = ('name', 'sap_id')
