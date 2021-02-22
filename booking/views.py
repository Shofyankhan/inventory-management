from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from store.models import Vechile

from .models import *

from .forms import *
from django.views import generic
from datetime import date, timedelta
import calendar
import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.core import serializers
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Sum

def vechilejsonlist(request):
    vechile = Vechile.objects.all().values('id','no_polisi', 'alias',)
    vechile_list = list(vechile)
    return JsonResponse(vechile_list, safe=False)

def bookinglistjson(request):    
    booking=Booking.objects.filter(status='active').values('resourceId', 'start', 'end', 'title', 'backgroundColor')
    bs = list(booking)

    return JsonResponse(bs, safe=False)


def autocomplete(request):
    if 'term' in request.GET:
        qs = Customer.objects.filter(no_hp__icontains=request.GET.get('term'))
        no_hps = list()
        
        no_hps = [customer.no_hp for customer in qs]
        return JsonResponse(no_hps, safe=False)
    return render(request, 'booking/create_book.html')

def autofill(request):
    if 'term' in request.GET:
        nh = Customer.objects.get()

    json.encoder

    data ={
        nama_pelanggan == Customer.nama_pelanggan()
    }

    pass

@login_required(login_url='login')
def create_customer(request):
    forms = CustomerForm()
    if request.method == 'POST':
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('customer-list')
        else:
            print(forms.errors)
    context = {
        'cform': forms
    }
    return render(request, 'booking/create_customer.html', context)

@login_required(login_url='login')
def create_payment(request):
    idbk = request.GET.get('idbooking')

    ibk = Booking.objects.get(idbooking=idbk)

    form = OrderForm(initial={
        'idbooking': idbk
    })

    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            nominal = form.cleaned_data['nominal_pembayaran']

            if nominal + ibk.dana_masuk == ibk.harga_jual:
                ibk.dana_masuk = nominal + ibk.dana_masuk
                ibk.backgroundColor = '#28a745'
                ibk.save()
            elif ibk.dana_masuk == 0:
                ibk.dana_masuk = nominal + ibk.dana_masuk
                ibk.backgroundColor = '#ffc107'
                ibk.save()
            elif ibk.dana_masuk > 0:
                ibk.dana_masuk = nominal + ibk.dana_masuk
                ibk.save()

            form.save()
            return redirect('book-list')
        else:
            print(form.errors)
    context = {
        'form': form,
        'ibk': ibk
    }
    return render(request, 'booking/create_payment.html', context)

@login_required(login_url='login')
def payment_history(request):
    idbk = request.GET.get('idbooking')
    paid = Booking.objects.get(idbooking=idbk)
    paid_order = paid.order_set.all().order_by('tanggal_pembayaran')

    context = {
        'paid':paid_order
    }
    return render(request, 'booking/history_payment_view.html', context)

class CustomerListView(ListView):
    model = Customer
    template_name = 'booking/customer_list.html'
    context_object_name = 'cus'

class BookingListView(ListView):
    model = Booking
    template_name = 'booking/book_list.html'
    context_object_name = 'book'

@login_required(login_url='login')
def create_book(request):
    try:
        booking_forms = BookingForm(initial={
            'resourceId': request.GET.get('resourceId'),
            'start': request.GET.get('start')
        })
    except:
        booking_forms = BookingForm()
    customer_forms = CustomerForm()
    if request.method == 'POST':
        booking_forms = BookingForm(request.POST)
        customer_forms = CustomerForm(request.POST)
        if customer_forms.is_valid() and booking_forms.is_valid():
            nama_pelanggan = customer_forms.cleaned_data['nama_pelanggan']
            no_hp = customer_forms.cleaned_data['no_hp']

            # nmpl = request.POST['nama_pelanggan']
            # nm_pl = {"nama_pelanggan": nmpl}

            customer, _ = Customer.objects.get_or_create(no_hp=customer_forms.cleaned_data['no_hp'],
            defaults={
                'nama_pelanggan': customer_forms.cleaned_data['nama_pelanggan'],
                'alamat_pelanggan': '',
                'tipe': ''
            },)

            idbooking = booking_forms.cleaned_data['idbooking']
            resourceId = booking_forms.cleaned_data['resourceId']
            start = booking_forms.cleaned_data['start']
            end = booking_forms.cleaned_data['end']
            harga_jual = booking_forms.cleaned_data['harga_jual']
            uang_jalan = booking_forms.cleaned_data['uang_jalan']
            parkir_bensin = booking_forms.cleaned_data['parkir_bensin']
            note = booking_forms.cleaned_data['note']

            Booking.objects.create(
                idbooking=idbooking,
                resourceId=resourceId,
                start=start,
                end=end+timedelta(days=1),
                end_date=end,
                harga_jual=harga_jual,
                uang_jalan=uang_jalan,
                parkir_bensin=parkir_bensin,
                note=note,
                title=resourceId,
                nm_pelanggan=Customer.objects.get(no_hp=no_hp),
            ),
            return redirect('booking-list')

        else:
            print(booking_forms.errors)
            print(customer_forms.errors)
        
    context = {
        'cform': customer_forms,
        'form': booking_forms,
    }

    return render(request, 'booking/create_book.html', context)

@login_required(login_url='login')
def booking_list(request):
    
    return render(request, 'booking/booking_list.html')

# AJAX
def load_customer(request):
    idbooking = request.GET.get('idbooking')
    harga_jual = Booking.objects.get(idbooking=idbooking)
    return render(request,  {'harga_jual': harga_jual})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)



# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()

# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month

# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month

# class CalendarView(LoginRequiredMixin, generic.ListView):
#     login_url = 'login'
#     model = Event
#     template_name = 'booking/create_booking.html'
# @login_required(login_url='login')
# def create_customer(request):
#     forms = CustomerForm()
#     if request.method == 'POST':
#         forms = CustomerForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('customer-list')
#         else:
#             print(forms.errors)
#     context = {
#         'cform': forms
#     }
#     return render(request, 'booking/create_customer.html', context)


# AJAX
def load_customer(request):
    nohp = request.GET.get('nohp')
    csm = Customer.objects.filter(nohp=nohp).all()
    return render(request, 'booking/customer_dropdown_list.html', {'csm': csm})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)







# def get_date(req_day):
#     if req_day:
#         return date(year, month, day=1)
#     return datetime.today()

# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month

# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month

# class CalendarView(LoginRequiredMixin, generic.ListView):
#     login_url = 'login'
#     model = Event
#     template_name = 'booking/create_booking.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get('month', None))
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         return context

