from django.db import models

from django.utils.timezone import now

# Create your models here.


class advertise(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')
    price = models.BigIntegerField()
    phone_number = models.BigIntegerField()
    post_date = models.DateField(default=now)
    location = models.CharField(max_length=80)

    class Meta:
        db_table = 'advertise'
        ordering = ['-post_date']

    def __str__(self):
        return f'{self.product_name}'
