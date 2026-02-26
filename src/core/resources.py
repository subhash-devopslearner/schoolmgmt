from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Student, AcademicClass

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