# Generated by Django 3.2.4 on 2021-06-13 03:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nidk', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name=datetime.datetime(2021, 6, 13, 3, 1, 11, 401012, tzinfo=utc))),
            ],
        ),
    ]