from django.db import models

class Internship(models.Model):
    student_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    roll_no = models.IntegerField()
    end_date = models.DateField()
    role= models.CharField(max_length=100, default='Intern')

class Meta:
    unique_together= ('company', 'roll_no')

    def __str__(self):
        return self.student_name
