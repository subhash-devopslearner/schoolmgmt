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
    ('Div-A', 'DIV-A'),
    ('Div-B', 'DIV-B'),
)

SEMESTER = (
    ('Sem-I', 'Semester I'),
    ('Sem-II', 'Semester II'),
    ('Sem-III', 'Semester III'),
    ('Sem-IV', 'Semester IV'),
    ('Sem-V', 'Semester V'),
    ('Sem-VI', 'Semester VI'),
    ('Sem-VII', 'Semester VII'),
    ('Sem-VIII', 'Semester VIII'),
)

TERMS = (
    ('I', 'Term-I'),
    ('II', 'Term-II'),
)

class AcademicYear(models.Model):
    academic_year = models.CharField(max_length=10) # 2025-2026
    is_current = models.BooleanField()       

    def __str__(self):
        return self.academic_year       

class AcademicTerm(models.Model):
    academic_term = models.CharField(choices=TERMS)
    term_startdate = models.DateField()
    term_enddate = models.DateField()

    def __str__(self):
        return self.academic_term

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=10)

    def __str__(self):
        return self.dept_name

class Class(models.Model):
    year = models.CharField(choices=YEAR)
    program = models.CharField(choices=PROGRAMS)
    branch = models.CharField(choices=BRANCHES)
    div = models.CharField(choices=DIVISON, blank=True)
    semester = models.CharField(choices=SEMESTER)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    academic_term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.program} {self.branch} {self.div} {self.semester}"








