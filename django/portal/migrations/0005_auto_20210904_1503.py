# Generated by Django 3.2.6 on 2021-09-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20210904_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pregnancy_month',
            field=models.IntegerField(default=None, null=True),
        ),
    ]