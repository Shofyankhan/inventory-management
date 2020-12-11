from django import forms

from .models import Season, Drop, Product, Order, Delivery, Vechile, VechileType, Vendor


class SupplierForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))

class BuyerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))


class VechileForm(forms.ModelForm):
    class Meta:
        model = Vechile
        fields = ['photo','no_polisi', 'alias', 'IDJenis', 'tanggal_stnk', 'status_stnk', 'tanggal_pembelian', 'harga_beli', 'scan_faktur_beli', 'vendor_id']

        widgets = {
            'no_polisi': forms.TextInput(attrs={'class': 'form-control', 'id': 'no_polisi', 'data-val': 'true',
                'data-val-required': 'Mohon Masukan Nomor Polisi !',}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'id': 'alias', 'required':'true'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'IDJenis': forms.Select(attrs={'class': 'form-control', 'id': 'IDJenis'}),
            'tanggal_stnk': forms.DateInput(attrs={'type': 'date', 'required':'true'}),
            'status_stnk': forms.Select(attrs={'class': 'form-control', 'id': 'status_stnk'}),
            'tanggal_pembelian': forms.DateInput(attrs={'type': 'date'}),
            'harga_beli': forms.TextInput(attrs={'class': 'form-control', 'id': 'harga_beli'}),
            'scan_faktur_beli': forms.FileInput(attrs={'class': 'form-control'}),
            'vendor_id': forms.Select(attrs={'class': 'form-control', 'id': 'vendor_id'}),
        }
        

class VechileTypeForm(forms.ModelForm):
    class Meta:
        model = VechileType
        fields = ['IDJenis', 'jenis', 'jumlah_seat', 'merek']

        widgets = {
            'IDJenis': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_jenis'}),
            'jenis': forms.Select(attrs={'class': 'form-control', 'id': 'jenis'}),
            'jumlah_seat': forms.NumberInput(attrs={'class': 'form-control', 'id': 'jumlah_seat'}),
            'merek': forms.TextInput(attrs={'class': 'form-control', 'id': 'merek'})
        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_id', 'nama_vendor', 'alamat_vendor', 'pic_vendor', 'notelp_kantor', 'notelp_pic']

        widgets = {
            'vendor_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'vendors_id'}),
            'nama_vendor': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama_vendor'}),
            'alamat_vendor': forms.TextInput(attrs={'class': 'form-control', 'id': 'alamat_vendor'}),
            'pic_vendor': forms.TextInput(attrs={'class': 'form-control', 'id': 'pic_vendor'}),
            'notelp_kantor': forms.TextInput(attrs={'class': 'form-control', 'id': 'notelp_kantor'}),
            'notelp_pic': forms.TextInput(attrs={'class': 'form-control', 'id': 'notelp_pic'})
        }


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'})
        }


class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sortno']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'sortno': forms.NumberInput(attrs={'class': 'form-control', 'id': 'sortno'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'product', 'design', 'color', 'buyer', 'season', 'drop']

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'design': forms.TextInput(attrs={'class': 'form-control', 'id': 'design'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'id': 'color'}),
            'buyer': forms.Select(attrs={'class': 'form-control', 'id': 'buyer'}),
            'season': forms.Select(attrs={'class': 'form-control', 'id': 'season'}),
            'drop': forms.Select(attrs={'class': 'form-control', 'id': 'drop'}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={'class': 'form-control', 'id': 'order'}),
            'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name'}),
        }
