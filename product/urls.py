from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import ProductsViewSet,Delete,ViewProductViewset


router = DefaultRouter()
router.register(r'Product_Profile', ProductsViewSet, basename='Product_Profile')
router.register(r'Delete_Product',Delete,basename='Delete_Product')
router.register(r'View_product',ViewProductViewset,basename="View_product")

urlpatterns = [
]+router.urls