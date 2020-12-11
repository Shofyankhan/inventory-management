from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta

from django.db.models import Q

from store.models import Product, Supplier, Buyer, Order, Vechile

@login_required(login_url='login')
def dashboard(request):
    total_vechile = Vechile.objects.count()
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    startdate = datetime.now()+timedelta(days=1)
    enddate = datetime.now()+timedelta(days=31)
    expired_stnk = Vechile.objects.filter(Q(tanggal_stnk__range = [startdate, enddate] ) | Q(tanggal_stnk__lte = datetime.now().date()))
    #tanggal_stnk__lte = datetime.now().date()
    context = {
        'vechile': total_vechile,
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder,
        'orders': orders,
        'expired_stnk' : expired_stnk
    }
    return render(request, 'dashboard.html', context)