from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/')

    class Meta:
        db_table = 'pages_category'

    def __str__(self):
        return f'{self.name}'


class products(models.Model):
    product_img = models.ImageField(upload_to='images/')
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=90, default='Kitoblar')
    price = models.BigIntegerField()
    phone_number = models.BigIntegerField()
    post_date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=80)

    class Meta:
        db_table = 'products'
        # ordering = ['-post_date']

    def str(self):
        return f'{self.product_name}'
