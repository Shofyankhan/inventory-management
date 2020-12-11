from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    create_supplier,
    create_buyer,
    create_vechile,
    edit_vechile,
    edit_vechile_type,
    edit_vendor,
    delete_vechile,
    delete_vechile_type,
    delete_vendor,
    create_vechile_type,
    create_vendor,
    create_season,
    create_drop,
    create_product,
    create_order,
    create_delivery,

    SupplierListView,
    BuyerListView,
    VechileListView,
    VechileTypeListView,
    VendorListView,
    VendorView,
    SeasonListView,
    DropListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-vechile/', create_vechile, name='create-vechile'),
    path('create-vechile-type/', create_vechile_type, name='create-vechile-type'),
    path('edit-vechile/<no_pol>', edit_vechile, name='edit-vechile'),
    path('delete-vechile/<no_pol>', delete_vechile, name='delete-vechile'),
    path('edit-vechile-type/<pk>', edit_vechile_type, name='edit-vechile-type'),
    path('delete-vechile-type/<pk>', delete_vechile_type, name='delete-vechile-type'),
    path('edit-vendor/<pk>', edit_vendor, name='edit-vendor'),
    path('delete-vendor/<pk>', delete_vendor, name='delete-vendor'),
    path('create-vendor/', create_vendor, name='create-vendor'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('arm-list/', VechileListView.as_view(), name='arm-list'),
    path('arm-type-list/', VechileTypeListView.as_view(), name='arm-type-list'),
    path('vendor-view/<ven_id>', VendorView, name='vendor-view'),
    path('vendor-list/', VendorListView.as_view(), name='vendor-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)