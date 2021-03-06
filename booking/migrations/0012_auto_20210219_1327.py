# Generated by Django 3.0.8 on 2021-02-19 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20210219_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='end_date',
            field=models.DateField(blank='True', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='nm_pelanggan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.Customer'),
        ),
    ]
