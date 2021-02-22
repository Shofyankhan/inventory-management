# Generated by Django 3.0.8 on 2021-02-17 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20210216_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, default='active', max_length=15),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal_pembayaran', models.DecimalField(decimal_places=0, max_digits=10)),
                ('pembayaran_ke', models.DecimalField(decimal_places=0, max_digits=10)),
                ('idbooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking')),
            ],
        ),
    ]
