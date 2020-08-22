from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    TeacherID = models.CharField(max_length=1000 , default = '-')
    TeacherName = models.CharField(max_length=1000 , default = '-')
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.TeacherName}'

class Student(models.Model):
    StudentID = models.CharField(max_length=1000 , default = '-')
    StudentName = models.CharField(max_length=1000 , default = '-')
    StudentGrade = models.CharField(max_length=1000 , default = '-')
    StudentRusalt = models.CharField(max_length=1000 , default = '-')
    StudentTotal = models.CharField(max_length=1000 , default = '-')
    StudentBirthday = models.DateField()
    ResposveTeacher = models.CharField(max_length=1000 , default='-')
    user = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.StudentName}'

class Subjects(models.Model):
    SubjectID = models.CharField(null=False,default='0',max_length=1000)
    SubjectName = models.CharField(null=False,default='UNKOWN',max_length=1000)
    SubjectTop = models.CharField(null=False,default='100',max_length=1000)
    SubjectLow = models.CharField(null=False,default='50',max_length=1000)
    FirstExam = models.CharField(null=False,default='0',max_length=100)
    SecExam = models.CharField(null=False,default='0',max_length=100)
    ThExam = models.CharField(null=False,default='0',max_length=100)
    FinalExam = models.CharField(null=False,default='0',max_length=100)
    OtherMarks = models.CharField(null=False,default='0',max_length=100)
    SubjectRusalt = models.CharField(null=False,default='-',max_length=1000)
    StudentID = models.CharField(null=False,max_length=1000,default='0')

    def __str__(self):
        return f'{self.SubjectName}'