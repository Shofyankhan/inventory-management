# Generated by Django 3.0.8 on 2020-12-13 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VechileType',
            fields=[
                ('jenis', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.CharField(max_length=10, unique=True)),
                ('nama_vendor', models.CharField(max_length=30, null=True)),
                ('alamat_vendor', models.CharField(blank='True', max_length=120, null=True)),
                ('pic_vendor', models.CharField(blank='True', max_length=15, null=True)),
                ('notelp_kantor', models.CharField(blank='True', max_length=15, null=True)),
                ('notelp_pic', models.CharField(blank='True', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vechile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_polisi', models.CharField(max_length=10, unique=True)),
                ('alias', models.CharField(max_length=20, null=True)),
                ('photo', models.ImageField(blank='True', null=True, upload_to='')),
                ('jumlah_seat', models.CharField(max_length=20, null=True)),
                ('merek', models.CharField(blank='True', choices=[('hino', 'Hino'), ('volvo', 'Volvo'), ('mercedes', 'Mercedes'), ('toyota', 'Toyota'), ('scania', 'Scania'), ('isuzu', 'Isuzu'), ('mitsubishi', 'Mitshubishi')], max_length=20, null=True)),
                ('tanggal_stnk', models.DateField(null=True)),
                ('tanggal_pembelian', models.DateField(blank='True', null=True)),
                ('harga_beli', models.DecimalField(blank='True', decimal_places=2, max_digits=6, null=True)),
                ('scan_faktur_beli', models.ImageField(blank='True', null=True, upload_to='')),
                ('jenis', models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.VechileType')),
                ('vendor_id', models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Vendor')),
            ],
        ),
    ]
