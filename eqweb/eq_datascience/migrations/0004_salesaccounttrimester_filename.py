# Generated by Django 2.2.4 on 2019-08-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eq_datascience', '0003_auto_20190818_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesaccounttrimester',
            name='filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
