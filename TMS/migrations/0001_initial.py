# Generated by Django 4.2.6 on 2023-10-07 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make', models.CharField(max_length=15)),
                ('car_model', models.CharField(max_length=15)),
                ('car_year_model', models.CharField(max_length=15)),
                ('car_short', models.CharField(max_length=20)),
                ('car_plate', models.CharField(max_length=20)),
                ('car_size', models.CharField(max_length=10)),
                ('car_mobile', models.CharField(max_length=10)),
                ('car_reg_nr', models.CharField(max_length=10)),
                ('car_reg_first', models.DateTimeField()),
                ('car_reg_due', models.DateTimeField()),
                ('car_stairs_due', models.DateTimeField()),
                ('car_lift_due', models.DateTimeField()),
                ('car_tires_due', models.DateTimeField()),
                ('fuel_card', models.CharField(max_length=20)),
                ('fuel_card_lastdigits', models.CharField(max_length=10)),
                ('car_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_fname', models.CharField(max_length=25)),
                ('driver_lname', models.CharField(max_length=25)),
                ('driver_short', models.CharField(max_length=25)),
                ('driver_mobile', models.CharField(max_length=15)),
                ('driver_email', models.CharField(max_length=50)),
                ('driver_cpr', models.CharField(max_length=15)),
                ('driver_address', models.CharField(max_length=100)),
                ('driver_bank_reg', models.CharField(max_length=10)),
                ('driver_bank_account', models.CharField(max_length=20)),
                ('driver_position', models.CharField(max_length=15)),
                ('fuel_card', models.CharField(max_length=20)),
                ('fuel_card_lastdigits', models.CharField(max_length=10)),
                ('driver_start', models.DateTimeField(auto_now_add=True)),
                ('driver_end', models.DateTimeField(auto_now_add=True)),
                ('driver_is_active', models.BooleanField()),
                ('driver_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcard_nr', models.CharField(max_length=25)),
                ('fcard_lastdigits', models.CharField(max_length=8)),
                ('fcard_type', models.CharField(max_length=5)),
                ('fcard_exp_date', models.DateTimeField()),
                ('fcard_is_active', models.BooleanField()),
                ('vl_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vl_id', models.CharField(max_length=8)),
                ('vl_nr', models.CharField(max_length=8)),
                ('vl_type', models.CharField(max_length=8)),
                ('vl_address', models.CharField(max_length=100)),
                ('vl_is_active', models.BooleanField()),
                ('vl_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
