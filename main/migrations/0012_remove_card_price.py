# Generated by Django 3.2.9 on 2021-12-11 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20211211_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='price',
        ),
    ]
