# Generated by Django 3.0.5 on 2020-07-07 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0009_auto_20200707_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 7, 20, 33, 0, 272361, tzinfo=utc)),
        ),
    ]
