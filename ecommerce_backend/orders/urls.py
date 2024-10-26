# orders/urls.py

from django.urls import path
from .views import PlaceOrderView, TrackOrderView, OrderHistoryView, InitiatePaymentView, UpdatePaymentStatusView
urlpatterns = [
    path('', PlaceOrderView.as_view(), name='place-order'),                # POST /orders/
    path('<int:pk>/', TrackOrderView.as_view(), name='track-order'),       # GET /orders/<id>/
    path('history/', OrderHistoryView.as_view(), name='order-history'),    # GET /orders/history/
    path('payments/', InitiatePaymentView.as_view(), name='initiate_payment'),   # POST /payments/
    path('payments/<int:pk>/', UpdatePaymentStatusView.as_view(), name='update_payment'),  # PUT /payments/<id>/
]
