# Generated by Django 3.0.8 on 2021-02-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_booking_dana_masuk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='harga_jual',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pembayaran_ke',
        ),
        migrations.AddField(
            model_name='order',
            name='tanggal_pembayaran',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
