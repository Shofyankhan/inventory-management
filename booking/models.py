from django.db import models
from django.urls import reverse
from store.models import Vechile
from datetime import date

import random

def random_string():
    return str(random.randint(10000, 99999))


class Customer(models.Model):
    TIPE_CHOICES = (
        ('agen', 'Agen'),
        ('perorangan', 'Perorangan'),
        ('perusahaan', 'Perusahaan'),
        ('instansi', 'Instansi'),
    )
    nama_pelanggan = models.CharField(max_length=35)
    alamat_pelanggan = models.CharField(max_length=220, blank='True')
    tipe = models.CharField(max_length=10, choices=TIPE_CHOICES, blank='True')
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_pelanggan

class Booking(models.Model):
    PAYMENT_STATUS = (
        ('#17a2b8', 'Pending'),
        ('#ffc107', 'Down Payment'),
        ('#28a745', 'Full Payment'),
    )
    idbooking = models.CharField(default = random_string, max_length=10, primary_key=True)
    resourceId = models.ForeignKey(Vechile, on_delete=models.SET_NULL, null=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    end_date = models.DateField(null=True, blank='True')
    harga_jual = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    dana_masuk = models.DecimalField(default = 0, max_digits=10, decimal_places=0)
    tanggal_pemesanan = models.DateField(auto_now_add=True)
    uang_jalan = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank='True')
    parkir_bensin = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank='True')
    note = models.CharField(max_length=15, null=True, blank='True')
    title = models.CharField(max_length=15, blank=True)
    backgroundColor = models.CharField(default = '#17a2b8', max_length=15, choices=PAYMENT_STATUS, blank=True)
    status = models.CharField(default='active', max_length=15, blank=True)

    nm_pelanggan = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.idbooking

class Order(models.Model):
    idbooking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    nominal_pembayaran = models.DecimalField(max_digits=10, decimal_places=0)
    tanggal_pembayaran = models.DateField(default=date.today)

    def __str__(self):
        return str(self.idbooking)


# # class Event(models.Model):
# #     start_time = models.DateTimeField()
# #     end_time = models.DateTimeField()
# #     created_date = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return self.created_date
    
# #     def get_absolute_url(self):
# #         return reverse('bookingapp:event-detail', args=(self.id,))

# #     @property
# #     def get_html_url(self):
# #         url = reverse('bookingapp:event-detail', args=(self.id,))
# #         return f'<a href="{url}"> {self.created_date} </a>'
