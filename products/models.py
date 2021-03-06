from django.db import models

# Create your models here.
class Product(models.Model):

# hackers could give  a long name
# name,price,stock and image are the attributes
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    # image_url = models.CharField(max_length=2083)
    product_image = models.ImageField(upload_to = 'products')
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()