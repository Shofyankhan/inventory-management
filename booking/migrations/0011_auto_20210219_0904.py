# Generated by Django 3.0.8 on 2021-02-19 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20210219_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='nm_pelanggan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.Customer'),
        ),
    ]
