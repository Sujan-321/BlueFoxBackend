# orders/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Payment
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404
from .serializers import PaymentSerializer

class PlaceOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the logged-in user to the order

class TrackOrderView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)  # Only allow access to user's own orders

class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)  # Filter to only the user's orders








# Initiate a payment for an order
class InitiatePaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the payment is linked to an existing order for the current user
        order_id = self.request.data.get('order')
        order = get_object_or_404(Order, id=order_id, user=self.request.user)
        serializer.save(order=order)

# Update payment status
class UpdatePaymentStatusView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ensure that only the owner of the order can update the payment
        payment = get_object_or_404(Payment, id=self.kwargs['pk'], order__user=self.request.user)
        return payment
    
    def update(self, request, *args, **kwargs):
        # Set partial=True to allow partial updates
        return super().update(request, *args, **kwargs, partial=True)
