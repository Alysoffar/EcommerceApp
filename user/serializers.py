from rest_framework import serializers # type: ignore
from .models import Customer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # type: ignore
from django.contrib.auth.hashers import make_password # type: ignore


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model, including password hashing.

    - Handles password validation and hashing during serialization.
    - Excludes the password field from deserialization to prevent accidental exposure.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        """
        Creates a new Employee instance, hashing the password before saving.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data) 
    
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

