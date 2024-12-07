from rest_framework import serializers # type: ignore
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # type: ignore
from django.contrib.auth.hashers import make_password # type: ignore

class ProductSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'image', 'stock')  # Adjust fields as needed
      
    