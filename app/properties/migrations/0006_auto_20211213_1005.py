# Generated by Django 3.2.8 on 2021-12-13 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20211213_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='i_occupy',
        ),
        migrations.RemoveField(
            model_name='property',
            name='year_occupied',
        ),
    ]
