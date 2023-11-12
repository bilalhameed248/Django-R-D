from django.db import models

# Create your models here.
class Product(models.Model):
	product_id=models.AutoField
	product_name=models.CharField(max_length=255)
	category=models.CharField(max_length=255, default="")
	sub_category=models.CharField(max_length=255, default="")
	price=models.IntegerField(default=0)
	desc=models.TextField()
	publish_date=models.DateField()
	image=models.ImageField(upload_to="shop/images", default="")

	def __str__(self):
		return self.product_name
	