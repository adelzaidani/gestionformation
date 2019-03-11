# Generated by Django 2.1.7 on 2019-03-11 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField(null=True)),
                ('postal_code', models.IntegerField(null=True)),
                ('locality', models.CharField(max_length=150)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('place_of_birth', models.CharField(max_length=150)),
                ('birth_date', models.DateField(null=True)),
                ('degree', models.CharField(max_length=150)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Etudiant'), (2, 'Formateur')], default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
