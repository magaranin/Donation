# Generated by Django 3.0.3 on 2022-05-30 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0021_receiveddonation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiveddonation',
            old_name='stripe_price_id',
            new_name='amount_id',
        ),
    ]
