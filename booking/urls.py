from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import(
    vechilejsonlist,
    autocomplete,

    create_customer,
    create_book,
    create_payment,

    bookinglistjson,

    booking_list,
    BookingListView,
    CustomerListView,
    payment_history,

    load_customer
)

appname = 'bookingapp'
urlpatterns = [
    path('vechilejson', vechilejsonlist, name='vechilejson'),
    path('bookingjson', bookinglistjson, name='bookingjson'),
    path('', autocomplete, name='autocomplete'),

    path('create-book/', create_book, name='create-book'),
    path('create-customer/', create_customer, name='create-customer'),
    path('create-payment/', create_payment, name='create-payment'),

    path('booking-list/', booking_list, name='booking-list'),
    path('customer-list/', CustomerListView.as_view(), name='customer-list'),
    path('book-list/', BookingListView.as_view(), name='book-list'),
    path('payment-history', payment_history, name='payment-history'),

    path('ajax/load-customer/', load_customer, name='ajax-load-customer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)