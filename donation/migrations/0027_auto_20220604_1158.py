# Generated by Django 3.0.3 on 2022-06-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0026_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.RemoveField(
            model_name='price',
            name='stripe_price_id',
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]