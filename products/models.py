from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=266, null=True, blank=True)
	category = models.CharField(max_length=266, null=True, blank=True)
	mode = models.CharField(max_length=200, null=True, blank=True, default= "Yard")
	sub_category = models.CharField(max_length=266, null=True, blank=True)
	initial_price = models.FloatField(null=True, blank=True)
	final_price = models.FloatField(null=True, blank=True)
	description = models.TextField(blank=True)
	original_pics = models.ImageField(null=True, blank=True, upload_to="images/")
	pics1 = models.ImageField(null=True, blank=True, upload_to="images/")
	pics2 = models.ImageField(null=True, blank=True, upload_to="images/")
	pics3 =  models.ImageField(null=True, blank=True, upload_to="images/")


	def __str__(self):
		return self.name +' '+ self.category+' '+ self.sub_category
 

class Cart(models.Model):
	product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
	user = models.ForeignKey(to=User, on_delete=models.CASCADE)


	def __str__(self):
		return self.user.username + ' carts '+ self.product.name


class Slide(models.Model):
	slide1pics = models.ImageField(null=True, blank=True, upload_to="slides/")
	slide1heading = models.CharField(max_length=250, null=True, blank=True)
	slide1subheading = models.CharField(max_length=250, null=True, blank=True)
	slide1writeup = models.CharField(max_length=250, null=True, blank=True)

	slide2pics = models.ImageField(null=True, blank=True, upload_to="slides/")
	slide2heading = models.CharField(max_length=250, null=True, blank=True)
	slide2subheading = models.CharField(max_length=250, null=True, blank=True)
	slide2writeup = models.CharField(max_length=250, null=True, blank=True)

	slide3pics = models.ImageField(null=True, blank=True, upload_to="slides/")
	slide3heading = models.CharField(max_length=250, null=True, blank=True)
	slide3subheading = models.CharField(max_length=250, null=True, blank=True)
	slide3writeup = models.CharField(max_length=250, null=True, blank=True)

	slide4pics = models.ImageField(null=True, blank=True, upload_to="slides/")
	slide4heading = models.CharField(max_length=250, null=True, blank=True)
	slide4subheading = models.CharField(max_length=250, null=True, blank=True)
	slide4writeup = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return self.slide1heading+' '+ self.slide2heading+' '+ self.slide3heading+' '+ self.slide4heading



