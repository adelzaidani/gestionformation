# Generated by Django 2.1.7 on 2019-05-25 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20190522_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='date_of_assessment',
        ),
    ]
