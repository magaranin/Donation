# Generated by Django 3.0.3 on 2022-05-02 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_user_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listingoffer',
            old_name='category',
            new_name='categories',
        ),
    ]