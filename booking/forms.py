from django import forms

from .models import *

from datetime import date, timedelta
from django.utils import timezone
from django.db.models import ExpressionWrapper, Q
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'nama_pelanggan': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama_pelanggan', }),
            'alamat_pelanggan': forms.TextInput(attrs={'class': 'form-control', 'id': 'alamat_pelanggan', }),
            'tipe': forms.Select(attrs={'class': 'form-control', 'id': 'tipe', }),
            'no_hp': forms.TextInput(attrs={'class': 'form-control', 'id': 'no_hp'}),
        }
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'idbooking': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'id_booking', 'style':'text-transform: uppercase'}),
            'resourceId': forms.Select(attrs={'class': 'form-control', 'id': 'no_polisi'}),
            'start' : forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'class': 'form-control', 'required':'true'}),
            'end' : forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'class': 'form-control', 'required':'true'}),
            'harga_jual': forms.NumberInput(attrs={'class': 'form-control', 'id': 'harga_jual'}),
            'uang_jalan': forms.NumberInput(attrs={'class': 'form-control', 'id': 'uang_jalan'}),
            'parkir_bensin': forms.NumberInput(attrs={'class': 'form-control', 'id': 'parkir_bensin'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'id': 'note'}),
            'dana_masuk': forms.HiddenInput(attrs={'class': 'form-control', 'id':'dana_masuk'}),
        }
    
    def clean(self):
        start = self.cleaned_data['start']
        end = self.cleaned_data['end']
        resourceId = self.cleaned_data['resourceId']

        # if start:
        #     st = Booking.objects.filter(start__range=[start, end], resourceId=resourceId)
        #     if st.exists():
        #         raise forms.ValidationError("Tanggal sudah dipesan dengan kendaraan yang sama!")
            
        # checking if date is not in the past,
        if start < date.today():
            raise forms.ValidationError("Tidak bisa memilih tanggal yang sudah lewat !")

        # checking end date must not higher than start date,
        if end < start:
            raise forms.ValidationError("Tanggal tiba tidak dapat lebih dulu dari tanggal berangkat !")



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'idbooking': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'id_booking',}),
            'nominal_pembayaran': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nominal_pembayaran', 'onclick': 'commas(self)'}),
            'tanggal_pembayaran': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'tanggal_pembayaran'})
        }
    def clean(self):
        idbooking = self.cleaned_data['idbooking']
        nominalp = self.cleaned_data['nominal_pembayaran']

        booking = Booking.objects.get(idbooking=idbooking)

        sisa = booking.harga_jual - booking.dana_masuk

        if nominalp > booking.harga_jual:
            raise forms.ValidationError("Nominal Pembayaran, tidak dapat melebihi nilai Harga Jual !")
        
        if nominalp > sisa:
            raise forms.ValidationError("Tidak dapat melebihi sisa pembayaran !")

    #     # reservation date avilable only for one yeer in future
    #     if start > date.today()+ timedelta(days=365):
    #         raise forms.ValidationError("Tidak dapat membuat pesanan untuk tahun depan !")

    #     #  cheacking if date for this bus is free
    #     res_all = Booking.objects.all()
    #     for item in res_all:
    #         if start >= item.start and start <= item.end  and item.resourceId == self.instance.resourceId:
    #             raise forms.ValidationError("This date is reserved for this bus, type another date or choose another bus.")
    #     # if Booking.objects.filter(start=start, end=self.instance.end, resourceId=self.instance.resourceId):
    #     #     raise forms.ValidationError("Tanggal ini sudah dipesan dengan tipe bus yang sama, silahkan pilih tanggal lain atau bus lain !")
    #     #set variable to send for next funtion: clean_EndDate
    #     self.tempReDate = start
    #     return start

    # def clean_end(self):
    #     #check if EndDate is empty
    #     if not self.data['end']:
    #         #set numbers days of reservation 1 if no end date
    #         self.instance.numOfDays =  1
    #         return None

    #     # if start date is empty
    #     if self.tempReDate == date(1,1,1):
    #         raise forms.ValidationError("Harus memilih tanggal berangkat !")

    #     # if start date is not empty
    #     else:
    #         start = self.tempReDate
    #         end = self.cleaned_data['end']

    #         # cheackig start date is not lower than end date
    #         if end < start:
    #             raise forms.ValidationError("Tanggal tiba tidak bisa lebih dulu dari tanggal berangkat !")

    #         # cheackig if reservation is no longer than 14 days
    #         if end > start+ timedelta(days=14):
    #             raise forms.ValidationError("You can make a reservation for max 14 days")

    #         #  cheacking if reservation  for this bus is free
    #         res_all = Booking.objects.all().filter(resourceId=self.instance.resourceId)
    #         for item in res_all:

    #             # czy rezerwacja od tego autobusu
    #             # if item.resourceId == self.instance.resourceId:

    #             #jesli w przedziale nowego zamowienia jest poczatek albo koniec innego to zajęte
    #             if start <= item.start and item.start <= end or start <= item.end and item.end <= end:
    #                 raise forms.ValidationError("Tanggal ini sudah dipesan dengan tipe bus yang sama, silahkan pilih tanggal lain atau bus lain !")

    #     # calculateing number  days of reservation and save it
    #     var = end - start
    #     self.instance.numOfDays = var.days + 1
    #     return start

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['nama_pelanggan'].queryset = Customer.objects.none()

    #     if 'country' in self.data:
    #         try:
    #             country_id = int(self.data.get('country'))
    #             self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
