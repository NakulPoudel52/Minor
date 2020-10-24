# Generated by Django 3.1.1 on 2020-10-24 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meeting_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_id', models.CharField(blank=True, max_length=25)),
                ('password', models.CharField(blank=True, max_length=25)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('meeting_name', models.TextField(blank=True, max_length=50)),
                ('receipt', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meessage_doctor', models.TextField(blank=True, max_length=500)),
                ('message_patient', models.TextField(blank=True, max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor')),
                ('meeting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.meeting_details')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='notification_for_patient',
            name='doctors',
        ),
        migrations.RemoveField(
            model_name='notification_for_patient',
            name='patients',
        ),
        migrations.DeleteModel(
            name='notification_for_doctor',
        ),
        migrations.DeleteModel(
            name='notification_for_patient',
        ),
    ]