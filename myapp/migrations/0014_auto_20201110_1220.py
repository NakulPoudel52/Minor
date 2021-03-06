# Generated by Django 3.1.1 on 2020-11-10 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20201104_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='meeting',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_detail', to='myapp.meeting_details'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timing', to='myapp.doctor_profile'),
        ),
    ]
