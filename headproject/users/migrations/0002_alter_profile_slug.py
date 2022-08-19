# Generated by Django 4.0.6 on 2022-08-19 20:03

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(null=True, unique_with=['user']),
        ),
    ]
