from .models import Order
from django.contrib.auth import logout # type: ignore
from .serializers import OrderSerializer,MyTokenObtainPairSerializer # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status, viewsets , mixins  # type: ignore
from rest_framework.permissions import IsAuthenticated , IsAdminUser,AllowAny # type: ignore
from rest_framework import generics  # type: ignore
from rest_framework.decorators import permission_classes  # type: ignore
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore




class OrderViewset(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,                   
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    permission_classes=[IsAuthenticated]
    
    def perform_create(self , serializer):
        serializer.save(user=self.request.user)

        product = serializer.validated_data['product']
        product.stock -= serializer.validated_data['quantity']
        product.save()


class Delete(viewsets.GenericViewSet, 
             mixins.DestroyModelMixin) :

    serializer_class=OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]  
     
