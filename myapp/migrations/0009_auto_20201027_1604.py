# Generated by Django 3.1.1 on 2020-10-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20201027_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.IntegerField(choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')], max_length=1),
        ),
    ]
