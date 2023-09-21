# Generated by Django 4.2.4 on 2023-09-19 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img', models.ImageField(upload_to='images/')),
                ('product_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.BigIntegerField()),
                ('phone_number', models.BigIntegerField()),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='gozallik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'gozallik',
            },
        ),
        migrations.CreateModel(
            name='ibodat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'ibodat',
            },
        ),
        migrations.CreateModel(
            name='kitoblar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'kitoblar',
            },
        ),
        migrations.CreateModel(
            name='offis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'offis',
            },
        ),
        migrations.CreateModel(
            name='parfyum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'parfyum',
            },
        ),
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
        migrations.CreateModel(
            name='salomatlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'salomatlik',
            },
        ),
        migrations.CreateModel(
            name='sovga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('location', models.CharField(max_length=90)),
                ('price', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'sovga',
            },
        ),
    ]
