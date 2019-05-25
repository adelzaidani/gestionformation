# Generated by Django 2.1.7 on 2019-05-09 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190509_0125'),
        ('billing', '0003_auto_20190509_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='booking',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='booking.RegistrationSession', verbose_name='Reservation'),
        ),
    ]
