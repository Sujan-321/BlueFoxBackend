# orders/serializers.py
from rest_framework import serializers
from .models import Order, Payment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product_name', 'quantity', 'price', 'status', 'order_date']
        read_only_fields = ['id', 'status', 'order_date']  # These fields should not be editable

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'status', 'payment_date']
        read_only_fields = ['id', 'payment_date']  # payment_date should be set automatically
