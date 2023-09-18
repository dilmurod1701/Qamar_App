# Generated by Django 4.2.5 on 2023-09-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_kitoblar'),
    ]

    operations = [
        migrations.CreateModel(
            name='quron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'quron',
            },
        ),
    ]