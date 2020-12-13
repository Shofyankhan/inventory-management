import xlwt

from django.shortcuts import render, redirect
from django.views.generic import ListView

from datetime import datetime, timedelta
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.utils.timezone import now

from django.http import HttpResponse
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Vechile, 
    VechileType,
    Vendor,
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery
)
from .forms import (
    VechileForm,
    VechileTypeForm,
    VendorForm,
    SupplierForm,
    BuyerForm,
    SeasonForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)



def VendorView(request, ven_id):
    vendors = Vendor.objects.get(vendor_id=ven_id)
    context = {
        'vendors': vendors
    }
    return render(request, 'store/vendor_view.html', context)


# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_supplier=True)
                Supplier.objects.create(user=user, name=name, address=address)
                return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Buyer views
@login_required(login_url='login')
def create_buyer(request):
    forms = BuyerForm()
    if request.method == 'POST':
        forms = BuyerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_buyer=True)
                Buyer.objects.create(user=user, name=name, address=address)
                return redirect('buyer-list')
        else:
            print(forms.errors)
    context = {
        'form': forms
    }
    return render(request, 'store/create_buyer.html', context)

class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'

####VECHILE#####

# vechile create (armada)
@login_required(login_url='login')
def create_vechile(request):
    forms = VechileForm()
    if request.method == 'POST':
        forms = VechileForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('arm-list')
        else:
            print(forms.errors)
    context = {
        'form': forms
    }
    return render(request, 'store/create_arm.html', context)


#update vechile armada
def edit_vechile(request, no_pol):
    armada = Vechile.objects.get(no_polisi=no_pol)
    vechileform = VechileForm(instance=armada)
    if request.method == 'POST':
        vechileform = VechileForm(request. POST,request.FILES, instance=armada)
        if vechileform.is_valid():
            vechileform.save()
            return redirect('arm-list')
        else:
            print(vechileform.errors)
    context = {
        'vechileform': vechileform
    }
    return render(request, 'store/edit_arm.html', context)


#update vechile armada
def edit_vechile_type(request, pk):
    armadatype = VechileType.objects.get(jenis=pk)
    vechiletypeform = VechileTypeForm(instance=armadatype)
    if request.method == 'POST':
        vechiletypeform = VechileTypeForm(request. POST,request.FILES, instance=armadatype)
        if vechiletypeform.is_valid():
            vechiletypeform.save()
        return redirect('arm-type-list')

    context = {
        'vechiletypeform': vechiletypeform
    }
    return render(request, 'store/edit_armtype.html', context)

# vechile armada
def delete_vechile_type(request, pk):
    armadatype = VechileType.objects.get(jenis=pk)
    armadatype.delete()
    return redirect('arm-type-list')
    #return render(request, 'store/arm_list.html')\


#update vechile armada
def edit_vendor(request, pk):
    vendora = Vendor.objects.get(vendor_id=pk)
    vendorform = VendorForm(instance=vendora)
    if request.method == 'POST':
        vendorform = VendorForm(request. POST,request.FILES, instance=vendora)
        if vendorform.is_valid():
            vendorform.save()
        return redirect('vendor-list')

    context = {
        'vendorform': vendorform
    }
    return render(request, 'store/edit_vendor.html', context)

#delete vechile armada
def delete_vendor(request, pk):
    vendora = Vendor.objects.get(vendor_id=pk)
    vendora.delete()
    return redirect('vendor-list')
    #return render(request, 'store/arm_list.html')



#delete vechile armada
def delete_vechile(request, no_pol):
    armada = Vechile.objects.get(no_polisi=no_pol)
    armada.delete()
    return redirect('arm-list')
    #return render(request, 'store/arm_list.html')


class VechileListView(ListView):
    model = Vechile
    template_name = 'store/arm_list.html'
    context_object_name = 'arm'

    def get_queryset(request):
        startdate = datetime.now()+timedelta(days=1)
        enddate = datetime.now()+timedelta(days=31)
        return Vechile.objects.annotate(
            expires_today=ExpressionWrapper(Q(tanggal_stnk__range = [startdate, enddate] ) | Q(tanggal_stnk__lte = datetime.now().date()), 
            output_field=BooleanField()))


#vechile type views
@login_required(login_url='login')
def create_vechile_type(request):
    forms = VechileTypeForm()
    if request.method == 'POST':
        forms = VechileTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('arm-type-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_arm_type.html', context)


class VechileTypeListView(ListView):
    model = VechileType
    template_name = 'store/arm_list_type.html'
    context_object_name = 'armtype'


# vendor views
@login_required(login_url='login')
def create_vendor(request):
    forms = VendorForm()
    if request.method == 'POST':
        forms = VendorForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('vendor-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_vendor.html', context)


class VendorListView(ListView):
    model = Vendor
    template_name = 'store/vendor_list.html'
    context_object_name = 'vendor'

# Season views
@login_required(login_url='login')
def create_season(request):
    forms = SeasonForm()
    if request.method == 'POST':
        forms = SeasonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('season-list')
        else:
            print(forms.errors)
    context = {
        'form': forms
    }
    return render(request, 'store/create_season.html', context)


class SeasonListView(ListView):
    model = Season
    template_name = 'store/season_list.html'
    context_object_name = 'season'


# Drop views
@login_required(login_url='login')
def create_drop(request):
    forms = DropForm()
    if request.method == 'POST':
        forms = DropForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('drop-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_drop.html', context)


class DropListView(ListView):
    model = Drop
    template_name = 'store/drop_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            color = forms.cleaned_data['color']
            buyer = forms.cleaned_data['buyer']
            season = forms.cleaned_data['season']
            drop = forms.cleaned_data['drop']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                color=color,
                buyer=buyer,
                season=season,
                drop=drop,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'