# Generated by Django 4.2.6 on 2023-10-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0005_alter_driver_end_alter_driver_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(max_length=25)),
                ('vl', models.CharField(max_length=8)),
                ('car', models.CharField(max_length=10)),
                ('income', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cash', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('p_type', models.CharField(max_length=8)),
                ('percent', models.IntegerField()),
                ('per_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fromdt', models.DateTimeField()),
                ('tilldt', models.DateTimeField()),
                ('work_time', models.DurationField()),
                ('pause', models.DurationField()),
                ('p_time', models.DurationField()),
                ('expenses', models.DecimalField(decimal_places=2, max_digits=6)),
                ('exp_reason', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.DateTimeField()),
            ],
        ),
    ]
