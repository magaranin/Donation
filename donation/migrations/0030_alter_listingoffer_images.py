# Generated by Django 4.0.4 on 2022-07-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0029_alter_gender_name_alter_whopays_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingoffer',
            name='images',
            field=models.FileField(blank=True, default=None, upload_to='images'),
        ),
    ]
