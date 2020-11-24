# Generated by Django 3.1.1 on 2020-10-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201027_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='BreakEndTime',
            field=models.TimeField(blank=True, default=2, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='BreakStartTime',
            field=models.TimeField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='EndTime',
            field=models.TimeField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='StartTime',
            field=models.TimeField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], max_length=1),
        ),
    ]