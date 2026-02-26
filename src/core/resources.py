from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Faculty, Student, AcademicClass, Department

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


class FacultyResource(resources.ModelResource):
    # This ensures the department is matched by 'dept_name' or 'dept_code' instead of ID
    department = fields.Field(
        column_name='department',
        attribute='department',
        widget=ForeignKeyWidget(Department, 'dept_name')
    )

    class Meta:
        model = Faculty        
        # Use employee_id as the unique identifier for updating existing records
        import_id_fields = ('name',)
        # Fields to include in import/export
        fields = ('salutation', 'name', 'department')