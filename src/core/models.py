from django.db import models

# Create your models here.
YEAR = (
    ('1st Year', 'FIRST YEAR'),
    ('2nd Year', 'SECOND YEAR'),
    ('3rd Year', 'THIRD YEAR'),
    ('4th Year', 'FOURTH YEAR'),
)

PROGRAMS = (
    ('BTech', 'BTECH'),
    ('MBATech', 'MBATECH'),
)

BRANCHES = (    
    ('CS', 'Computer Science'),
    ('CE', 'Computer Engineering'),
    ('IT', 'Information Technology'),
    ('AIML', 'Artificial Intelligence and Machine Learning'),
    ('CSEDS', 'Computer Science Engineering (Data Science)'),
)

DIVISON = (
    ('Div A', 'DIV-A'),
    ('Div B', 'DIV-B'),
)

SEMESTER = (
    ('Sem I', 'Semester I'),
    ('Sem II', 'Semester II'),
    ('Sem III', 'Semester III'),
    ('Sem IV', 'Semester IV'),
    ('Sem V', 'Semester V'),
    ('Sem VI', 'Semester VI'),
    ('Sem VII', 'Semester VII'),
    ('Sem VIII', 'Semester VIII'),
)

TERMS = (
    ('Term-I', 'TERM-I'),
    ('Term-II', 'TERM-II'),
)

SALUTATIONS = (
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof.'),
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
)


class AcademicYear(models.Model):
    academic_year = models.CharField(max_length=10) # 2025-2026
    is_current = models.BooleanField()       

    def __str__(self):
        return self.academic_year    
       

class AcademicTerm(models.Model):
    academic_term = models.CharField(max_length=10, choices=TERMS)
    term_startdate = models.DateField()
    term_enddate = models.DateField()

    def __str__(self):
        return self.academic_term
    

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=10)

    def __str__(self):
        return self.dept_name
    

class AcademicClass(models.Model):
    year = models.CharField(max_length=20, choices=YEAR)
    program = models.CharField(max_length=20, choices=PROGRAMS)
    branch = models.CharField(max_length=10, choices=BRANCHES)
    div = models.CharField(max_length=10, choices=DIVISON, blank=True)
    semester = models.CharField(max_length=10, choices=SEMESTER)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    academic_term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)    
    class_name = models.CharField(max_length=255, unique=True, editable=False)

    class Meta:
        # Ensures you don't accidentally create the same Div for the same Sem/Year twice
        unique_together = ('program', 'branch', 'semester', 'div')

    def save(self, *args, **kwargs):
        # Added Academic Year to make it truly unique
        self.class_name = f"{self.program} {self.branch} {self.semester} {self.div} ({self.academic_year.academic_year})"
        super().save(*args, **kwargs)   

    def __str__(self):
        return self.class_name
        
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=5)
    sap_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    class_enrolled = models.ForeignKey(AcademicClass, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
    
    
class Faculty(models.Model):
    salutation = models.CharField(max_length=10, choices=SALUTATIONS)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)    

    def __str__(self):
        return f"{self.salutation} {self.name} ({self.employee_id})"
    
    
class Subject(models.Model):
    subject_code = models.CharField(max_length=10, unique=True)
    subject_name = models.CharField(max_length=100)
    class_associated = models.ForeignKey(AcademicClass, on_delete=models.SET_NULL, null=True, related_name='subjects') 
    faculty_assigned = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, related_name='subjects_taught')   

    class Meta:
        # Ensures a subject code is unique within a specific class
        unique_together = ('subject_code', 'class_associated')

    def __str__(self):
        return f"{self.subject_name} ({self.class_associated})"
