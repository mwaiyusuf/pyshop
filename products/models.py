from django.db import models

# Create your models here.
class Product(models.Model):
# hackers could give  a long name
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_lenght=2083)