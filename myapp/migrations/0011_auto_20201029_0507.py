# Generated by Django 3.1.1 on 2020-10-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20201027_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_profile',
            name='NMC_ID',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='BreakEndTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='BreakStartTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='EndTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='StartTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
