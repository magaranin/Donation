# Generated by Django 3.0.3 on 2022-06-01 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0022_auto_20220530_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiveddonation',
            old_name='amount',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='receiveddonation',
            old_name='amount_id',
            new_name='price_id',
        ),
    ]
