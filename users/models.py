from django.db import models


class CreateAccount(models.Model):
    last_name = models.CharField(max_length=55)
    first_name = models.CharField(max_length=55)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=70)
    password1 = models.CharField(max_length=33)
    password2 = models.CharField(max_length=33)

    class Meta:
        db_table = 'CreateAccount'

    def __str__(self):
        return f'New user {self.username}!'
