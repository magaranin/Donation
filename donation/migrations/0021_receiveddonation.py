# Generated by Django 3.0.3 on 2022-05-30 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0020_listingoffer_claimed_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stripe_price_id', models.CharField(max_length=100)),
            ],
        ),
    ]
