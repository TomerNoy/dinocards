# Generated by Django 3.2.9 on 2021-12-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_date_transaction_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dino',
            name='rarity_rate',
            field=models.PositiveIntegerField(choices=[('C', 100), ('M', 500), ('R', 800), ('V', 1000)]),
        ),
    ]
