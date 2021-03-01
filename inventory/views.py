from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta

from django.db.models import Q

from store.models import Product, Supplier, Buyer, Vechile
from booking.models import Booking, Customer, Order

@login_required(login_url='login')
def dashboard(request):
    startdate = datetime.now()+timedelta(days=1)
    enddate = datetime.now()+timedelta(days=31)

    startrecent = datetime.now()
    endrecent = datetime.now()+timedelta(days=4)

    total_vechile = Vechile.objects.count()
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_customer = Customer.objects.count()
    total_booking = Booking.objects.count()

    # total_order = Order.objects.count()
    # orders = Order.objects.all().order_by('-id')

    expired_stnk = Vechile.objects.filter(Q(tanggal_stnk__range = [startdate, enddate] ) | Q(tanggal_stnk__lte = datetime.now().date()))
    recent_order = Booking.objects.filter(Q(start__range = [startrecent, endrecent]))

    context = {
        'vechile': total_vechile,
        'product': total_product,
        'supplier': total_supplier,
        'customer': total_customer,
        'booking': total_booking,
        # 'order': total_oder,
        # 'orders': orders,
        'recent_order': recent_order,
        'expired_stnk' : expired_stnk
    }
    return render(request, 'dashboard.html', context)