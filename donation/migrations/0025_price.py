# Generated by Django 3.0.3 on 2022-06-03 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0024_delete_receiveddonation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_price_id', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]