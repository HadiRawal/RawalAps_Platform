# Generated by Django 4.2.6 on 2023-10-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0007_remove_trip_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='start',
            field=models.DateField(blank=True),
        ),
    ]
