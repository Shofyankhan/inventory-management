from django.db import models

from users.models import User

class Vendor(models.Model):
    vendor_id = models.CharField(max_length=10, unique=True)
    nama_vendor = models.CharField(max_length=30, null=True)
    alamat_vendor = models.CharField(max_length=120, null=True, blank='True')
    pic_vendor = models.CharField(max_length=15, null=True, blank='True')
    notelp_kantor = models.CharField(max_length=15, null=True, blank='True')
    notelp_pic = models.CharField(max_length=15, null=True, blank='True')

    def save(self, force_insert=False, force_update=False):
        self.vendor_id = self.vendor_id.upper()
        self.nama_vendor = self.nama_vendor.upper()
        self.pic_vendor = self.pic_vendor.upper()
        self.notelp_kantor = self.notelp_kantor.upper()
        self.notelp_pic = self.notelp_pic.upper()
        super(Vendor, self).save(force_insert, force_update)

    def __str__(self):
        return self.vendor_id

class VechileType(models.Model):
    jenis = models.CharField(max_length=20, primary_key=True)

    def save(self, force_insert=False, force_update=False):
        self.jenis = self.jenis.upper()
        super(VechileType, self).save(force_insert, force_update)

    def __str__(self):
        return self.jenis

class Vechile(models.Model):
    MERK_CHOICE = (
        ('hino', 'Hino'),
        ('volvo', 'Volvo'),
        ('mercedes', 'Mercedes'),
        ('toyota', 'Toyota'),
        ('scania', 'Scania'),
        ('isuzu', 'Isuzu'),
        ('mitsubishi', 'Mitshubishi'),
    )
    no_polisi = models.CharField(max_length=10, unique=True)
    alias = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='', null=True, blank='True')
    jenis = models.ForeignKey(VechileType, on_delete=models.SET_NULL, null=True, blank='True')
    jumlah_seat = models.PositiveIntegerField(blank=True, null=True)
    merek = models.CharField(max_length=20, null=True, blank='True', choices=MERK_CHOICE)
    tanggal_stnk = models.DateField(null=True)
    tanggal_pembelian = models.DateField(null=True, blank='True')
    harga_beli = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank='True')
    scan_faktur_beli = models.ImageField(upload_to='', null=True, blank='True')
    vendor_id = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank='True')

    def save(self, force_insert=False, force_update=False):
        self.no_polisi = self.no_polisi.upper()
        self.alias = self.alias.upper()
        super(Vechile, self).save(force_insert, force_update)

    def __str__(self):
        return self.no_polisi


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name