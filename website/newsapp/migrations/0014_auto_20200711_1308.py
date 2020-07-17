# Generated by Django 3.0.5 on 2020-07-11 12:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0013_auto_20200709_1457'),
    ]

    operations = [
        migrations.DeleteModel(
            name='home_news2',
        ),
        migrations.DeleteModel(
            name='home_news3',
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 11, 12, 8, 31, 32456, tzinfo=utc)),
        ),
    ]
