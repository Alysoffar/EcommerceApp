from django.db import models  # type: ignore

# Create your models here.

class Product(models.Model):
    """
    Model for Products in the database.
    """
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField(blank=True)  # Optional product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    stock = models.PositiveIntegerField(default=0)  # Available product stock
    image = models.ImageField(upload_to='products/', default='default.jpg', blank=True,null=True)  # Product image
    # Additional product attributes can be added here

    def __str__(self):
        return self.name  # String representation of a product object