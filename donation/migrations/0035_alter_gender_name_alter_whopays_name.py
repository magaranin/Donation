# Generated by Django 4.0.4 on 2022-07-24 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0034_alter_listingoffer_delivery_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='whopays',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]