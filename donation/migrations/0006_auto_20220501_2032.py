# Generated by Django 3.0.3 on 2022-05-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0005_auto_20220501_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingoffer',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
