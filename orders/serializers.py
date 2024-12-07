import datetime
from rest_framework import serializers # type: ignore
from .models import Order
from product.models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.hashers import make_password # type: ignore


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    delivery_date = serializers.DateTimeField(default=timezone.now) 

    class Meta:
        model = Order
        fields = '__all__'

    def validate_delivery_date(self, value):
        # Ensure delivery date is in the future
        if value <= datetime.date.today():
            raise serializers.ValidationError("Delivery date must be in the future")
        return value
    
    def validate_Stock(self, data):
        product = data['product']
        quantity = data['quantity']

        if quantity > product.stock:
            raise serializers.ValidationError("Insufficient stock for this product.")

        return data
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

