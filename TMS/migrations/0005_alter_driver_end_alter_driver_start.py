# Generated by Django 4.2.6 on 2023-10-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0004_alter_car_created_at_alter_driver_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='start',
            field=models.DateField(),
        ),
    ]
