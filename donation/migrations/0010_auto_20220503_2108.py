# Generated by Django 3.0.3 on 2022-05-04 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0009_auto_20220502_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
    ]