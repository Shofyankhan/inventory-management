# Generated by Django 3.0.8 on 2021-02-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210214_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='nm_pelanggan',
            field=models.CharField(blank='True', max_length=35, null=True),
        ),
    ]
