# Generated by Django 3.2.9 on 2021-12-09 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_deck_offer_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='date',
            new_name='date_created',
        ),
    ]
