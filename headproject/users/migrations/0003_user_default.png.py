# Generated by Django 4.0.6 on 2022-07-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='default.png',
            field=models.ImageField(blank=True, upload_to='', verbose_name='photo'),
        ),
    ]