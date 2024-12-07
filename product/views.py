from .models import Product
from django.contrib.auth import logout # type: ignore
from .serializers import ProductSerializer
from rest_framework import status, viewsets , mixins  # type: ignore
from rest_framework.permissions import IsAuthenticated , IsAdminUser # type: ignore
from rest_framework import generics  # type: ignore
from rest_framework.response import Response  # type: ignore

class ViewProductViewset(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    permission_classes=[IsAuthenticated]

class ProductsViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):

    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        # Handle product creation logic here
        return super().create(request, *args, **kwargs)
    
    
    def get_permissions(self):
        if self.action == 'create':
            if self.request.user.is_superuser:
                return []  # Allow superusers (no explicit permissions needed)
            return super().get_permissions()
        return super().get_permissions()

    def get_queryset(self):
        """
        Filters the queryset based on the desired criteria.

        You can customize the filtering logic to return the products you want.
        For example, you might filter based on product category, price range,
        availability, or other relevant attributes.
        """

        # Replace the following with your desired filtering logic:
        queryset = Product.objects.all()

        '''# Example filtering based on product category:
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)'''

        # Example filtering based on price range:
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        return queryset
    def update(self, request, *args, **kwargs):
        """
        Handles the product update request.

        You can customize the update logic to modify specific product attributes.
        """

        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data)
        serializer.is_valid(raise_exception=True) 


        # Customize the update logic here:
        product.name = serializer.validated_data.get('name', product.name)
        product.price = serializer.validated_data.get('price', product.price)
        # Add more attribute updates as needed

        product.save()
        return Response(serializer.data)

class Delete(viewsets.GenericViewSet, 
             mixins.DestroyModelMixin) :

    serializer_class=ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]  
     