# Generated by Django 3.0.8 on 2021-02-15 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20210215_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='active', max_length=15),
        ),
        migrations.AlterField(
            model_name='booking',
            name='backgroundColor',
            field=models.CharField(blank=True, choices=[('blue', 'Pending'), ('yellow', 'Down Payment'), ('green', 'Full Payment')], default='blue', max_length=15),
        ),
    ]
