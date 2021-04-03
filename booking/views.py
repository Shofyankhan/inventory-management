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
from django import forms
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def payment_render_pdf_view(request, *args, **kwargs): 
    pk = kwargs.get('pk')
    datas = get_object_or_404(Order, id=pk)
    booking = Booking.objects.get(idbooking=datas.idbooking)

    template_path = 'booking/payment.html'
    context = {
        'datas': datas,
        'booking': booking
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #for download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #for displays
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def booking_render_pdf_view(request, *args, **kwargs): 
    pk = kwargs.get('pk')
    datas = get_object_or_404(Booking, idbooking=pk)
    booking = Booking.objects.get(idbooking=datas.idbooking)

    template_path = 'booking/booking_pdf.html'
    context = {
        'datas': datas,
        'booking': booking
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #for download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #for displays
    response['Content-Disposition'] = 'filename="booking.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'booking/payment.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #for download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #for displays
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def vechilejsonlist(request):
    vechile = Vechile.objects.all().values('id','no_polisi', 'alias',)
    vechile_list = list(vechile)
    return Jso

def render_pdf_view(request):
    template_path = 'booking/payment.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #for download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #for displays
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def vechilejsonlist(request):
    vechile = Vechile.objects.all().values('id','no_polisi', 'alias',)
    vechile_list = list(vechile)
    return JsonResponse(vechile_list, safe=False)

def bookinglistjson(request):    
    booking=BonResponse(vechile_list, safe=False)

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

#create customer
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

#show customer
class CustomerListView(ListView):
    model = Customer
    template_name = 'booking/customer_list.html'
    context_object_name = 'cus'

#update customer
def edit_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request. POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer-list')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_customer.html', context)


#delete customer
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect('customer-list')
    #return render(request, 'store/arm_list.html')\


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
        'data':paid,
        'paid':paid_order
    }
    return render(request, 'booking/history_payment_view.html', context)

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

            customer, _ = Customer.objects.get_or_create(no_hp=customer_forms.cleaned_data['no_hp'],
            defaults={
                'nama_pelanggan': customer_forms.cleaned_data['nama_pelanggan'],
                'alamat_pelanggan': '',
                'tipe': ''
            },)

            idbooking = booking_forms.cleaned_data['idbooking']
            resourceId = booking_forms.cleaned_data['resourceId']
            start = booking_forms.cleaned_data['start']
            end_date = booking_forms.cleaned_data['end_date']
            harga_jual = booking_forms.cleaned_data['harga_jual']
            uang_jalan = booking_forms.cleaned_data['uang_jalan']
            parkir_bensin = booking_forms.cleaned_data['parkir_bensin']
            note = booking_forms.cleaned_data['note']

            Booking.objects.create(
                idbooking=idbooking,
                resourceId=resourceId,
                start=start,
                end_date=end_date,
                end=end_date+timedelta(days=1),
                harga_jual=harga_jual,
                uang_jalan=uang_jalan,
                parkir_bensin=parkir_bensin,
                note=note,
                title=idbooking,
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
def edit_book(request, pk):
    booking = Booking.objects.get(idbooking=pk)
    booking_forms = BookingEditForm(instance=booking)
    customer_forms = CustomerForm(initial={
            'no_hp': request.GET.get('no_hp'),
            'nama_pelanggan': request.GET.get('nama_pelanggan')
        })
    if request.method == 'POST':
        booking_forms = BookingEditForm(request.POST)
        if booking_forms.is_valid():

            resourceId = booking_forms.cleaned_data['resourceId']
            start = booking_forms.cleaned_data['start']
            end_date = booking_forms.cleaned_data['end_date']
            harga_jual = booking_forms.cleaned_data['harga_jual']
            uang_jalan = booking_forms.cleaned_data['uang_jalan']
            parkir_bensin = booking_forms.cleaned_data['parkir_bensin']
            note = booking_forms.cleaned_data['note']

            Booking.objects.filter(idbooking=booking).update(
                resourceId=resourceId,
                start=start,
                end_date=end_date,
                end=end_date+timedelta(days=1),
                harga_jual=harga_jual,
                uang_jalan=uang_jalan,
                parkir_bensin=parkir_bensin,
                note=note,
            ),
            return redirect('booking-list')

        else:
            print(booking_forms.errors)

    context = {
        'cform': customer_forms,
        'form': booking_forms,
    }

    return render(request, 'booking/create_book.html', context)

def delete_book(request, pk):
    booking = Booking.objects.get(idbooking=pk)
    booking.delete()
    return redirect('booking-list')


@login_required(login_url='login')
def booking_list(request):
    
    return render(request, 'booking/booking_list.html')


@login_required(login_url='login')
def booking_detail_view(request):
    idbook = request.GET.get('idbooking')
    form = Booking.objects.get(idbooking=idbook)
    paid_order = form.order_set.all()
    context = {
        'form': form,
        'cform': paid_order
    }
    return render(request, 'booking/booking_detail.html', context)


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

