# Generated by Django 3.0.3 on 2022-05-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_auto_20220501_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingoffer',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]