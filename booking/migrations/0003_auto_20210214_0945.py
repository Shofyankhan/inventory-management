# Generated by Django 3.0.8 on 2021-02-14 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20210213_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='nama_pelanggan',
            new_name='nm_pelanggan',
        ),
    ]