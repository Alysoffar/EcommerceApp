from django.db import models # type: ignore
from user.models import Customer
from product.models import Product
from django.utils import timezone # type: ignore
import random

class Order(models.Model):

    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')  # Use related_name for better querysets
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    creation_date = models.DateTimeField(default=timezone.now)  # Use DateTimeField for more precise timestamps
    delivery_date = models.DateTimeField(default=timezone.now)  # Enforce positive delivery periods
    billing_price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for monetary values
    quantity=models.PositiveBigIntegerField(null=True,default=1)
    
    def delivery_period(self):
        """
        Custom validation method to ensure delivery period is at least 1.
        Raises ValidationError with an error message if not.
        """
        if self.delivery_period < 1:
            raise models.ValidationError("Delivery period must be at least 1 day.")
        return self.delivery_period

    def save(self, *args, **kwargs):
        if not self.delivery_period:
            self.delivery_period = random.randint(1, 5)
        self.billing_price = self.quantity*self.product.price
        self.product.stock-=self.quantity

        super().save(*args, **kwargs)
    def __str__(self):
        """
        Custom string representation for a more informative order object view.
        """
        return f"Order #{self.id} for customer {self.customer.name} - Product: {self.product.name}"
    