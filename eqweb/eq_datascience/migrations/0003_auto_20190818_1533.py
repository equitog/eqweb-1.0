# Generated by Django 2.2.4 on 2019-08-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eq_datascience', '0002_remove_cuenta_logo_cuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesAccountTrimester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('trimester', models.SmallIntegerField(blank=True, null=True)),
                ('sales', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='date_until',
            field=models.DateTimeField(blank=True, help_text='Ingrese la fecha de inactividad para la cuenta.', null=True, verbose_name='Fecha de Inactividad'),
        ),
    ]
