# Generated by Django 3.1.1 on 2020-10-20 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Denru', '0002_auto_20201019_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkcode',
            name='phone',
        ),
    ]