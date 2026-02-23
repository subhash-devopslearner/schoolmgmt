from django.contrib import admin
from .models import AcademicYear, AcademicTerm, Class

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(AcademicTerm)
admin.site.register(Class)