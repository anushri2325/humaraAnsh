# Generated by Django 3.2.6 on 2021-09-04 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_teacher',
            new_name='is_doctor',
        ),
    ]