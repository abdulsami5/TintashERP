# Generated by Django 2.0.7 on 2018-08-10 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loghours', '0005_auto_20180810_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loghours',
            name='project_loghour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loghours.ProjectLogHour'),
        ),
    ]
