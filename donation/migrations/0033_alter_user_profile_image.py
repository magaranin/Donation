# Generated by Django 4.0.4 on 2022-07-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0032_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='images/default.jpg', upload_to='profile_images'),
        ),
    ]
