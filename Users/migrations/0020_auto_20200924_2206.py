# Generated by Django 3.0.8 on 2020-09-24 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0019_treatment_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Specialization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='Doctors', to='Users.Specialization'),
        ),
    ]
