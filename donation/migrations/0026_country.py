# Generated by Django 3.0.3 on 2022-06-04 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0025_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='United States', max_length=30)),
            ],
        ),
    ]