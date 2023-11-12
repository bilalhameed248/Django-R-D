from django.db import models

# Create your models here.
class Section(models.Model):
    section_title=models.CharField(max_length=50)

    def __str__(self):
        return self.section_title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)