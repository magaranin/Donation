# Generated by Django 3.0.3 on 2022-05-02 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0007_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingoffer',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donation.Gender'),
        ),
    ]