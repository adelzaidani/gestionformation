# Generated by Django 2.1.7 on 2019-05-08 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_auto_20190509_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation', models.CharField(max_length=100, verbose_name='Formation')),
                ('date', models.DateField(null=True, verbose_name='Date de facturation')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Payable'), (2, 'Payer'), (3, 'Annuler')], default=1, verbose_name='Statut')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Prix')),
                ('client', models.ForeignKey(limit_choices_to={'user_type': 1}, on_delete=django.db.models.deletion.CASCADE, to='account.Profile', verbose_name='Etudiant')),
            ],
        ),
    ]