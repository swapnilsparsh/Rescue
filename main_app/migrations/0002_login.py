# Generated by Django 3.1.5 on 2021-03-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username_or_Email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
