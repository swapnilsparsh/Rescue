# Generated by Django 3.1.1 on 2021-03-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210324_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]