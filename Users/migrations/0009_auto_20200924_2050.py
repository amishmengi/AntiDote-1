# Generated by Django 3.0.8 on 2020-09-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_auto_20200924_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='Appointment',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='Prescription',
            field=models.TextField(blank=True, default=None, max_length=800, null=True),
        ),
    ]
