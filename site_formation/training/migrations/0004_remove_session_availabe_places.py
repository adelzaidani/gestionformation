# Generated by Django 2.1.7 on 2019-03-31 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_auto_20190315_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='availabe_places',
        ),
    ]
