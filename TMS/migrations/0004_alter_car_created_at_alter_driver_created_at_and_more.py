# Generated by Django 4.2.6 on 2023-10-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0003_alter_car_created_at_alter_car_lift_due_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fcard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]