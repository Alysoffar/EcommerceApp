
from .models import Customer
from django.contrib.auth import logout # type: ignore
from .serializers import CustomerSerializer,MyTokenObtainPairSerializer # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status, viewsets , mixins  # type: ignore
from rest_framework.permissions import IsAuthenticated , IsAdminUser,AllowAny # type: ignore
from rest_framework import generics  # type: ignore
from rest_framework.decorators import permission_classes  # type: ignore
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore


class MyObtainTokenPairView(TokenObtainPairView):
    #permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


@permission_classes([IsAuthenticated])    
class Logout(generics.GenericAPIView):
    def logout(request):
        serializer = CustomerSerializer
        logout(request)
        return Response('Logged out!') 


class CustomerViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):

    serializer_class = CustomerSerializer
    permission_classes =[AllowAny]
    def get_queryset(self):
        """
        Filters the queryset to return only the objects for the currently authenticated user
        if the action is 'retrieve', 'update', or 'list'.
        """
        if self.action in ['retrieve', 'update', 'list']:
            return Customer.objects.filter(user=self.request.user)
        return Customer.objects.all()


