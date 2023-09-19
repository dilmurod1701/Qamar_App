from django.db import models

from django.utils.timezone import now

# Create your models here.

class ad(models.Model):
    product_img = models.ImageField(upload_to='images/')
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.BigIntegerField()
    phone_number = models.BigIntegerField()
    post_date = models.DateField(default=now)
    location = models.CharField(max_length=80)

    class Meta:
        db_table = 'products'
        # ordering = ['-post_date']

    def str(self):
        return f'{self.product_name}'

class salomatlik(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'salomatlik'

    def __str__(self):
        return f'{self.title}'


class kitoblar(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'kitoblar'

    def __str__(self):
        return f'{self.title}'


class quron(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'quron'

    def __str__(self):
        return f'{self.title}'


class offis(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'offis'

    def __str__(self):
        return f'{self.title}'


class ibodat(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'ibodat'

    def __str__(self):
        return f'{self.title}'


class sovga(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'sovga'

    def __str__(self):
        return f'{self.title}'


class parfyum(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'parfyum'

    def __str__(self):
        return f'{self.title}'


class gozallik(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=90)
    price = models.CharField(max_length=90)

    class Meta:
        db_table = 'gozallik'

    def __str__(self):
        return f'{self.title}'


