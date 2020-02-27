from django.contrib import admin
from .models import Product, offer
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock")

admin.site.register(Product, ProductAdmin)