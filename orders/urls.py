from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import OrderViewset,Delete

router = DefaultRouter()
router.register(r'Order',OrderViewset,basename="Order")
router.register(r'Delete',Delete,basename="Delete")


urlpatterns = [
]+router.urls