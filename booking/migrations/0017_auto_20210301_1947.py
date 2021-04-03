# Generated by Django 3.0.8 on 2021-03-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_auto_20210221_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='harga_jual',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.DateField(null=True),
        ),
    ]