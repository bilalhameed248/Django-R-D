from django.db import models

# Create your models here.
class personal_info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    upload = models.FileField(upload_to ='cv/') 

    class Meta:
        db_table = 'personal_info'