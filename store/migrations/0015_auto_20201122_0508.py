# Generated by Django 3.0.8 on 2020-11-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20201122_0401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vechiletype',
            name='id',
        ),
        migrations.AlterField(
            model_name='vechiletype',
            name='IDJenis',
            field=models.TextField(max_length=10, primary_key=True, serialize=False),
        ),
    ]