from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    # Add other customer-specific fields here

    def __str__(self):
        return self.user.username  # Or a more descriptive representation

    class Meta:
        verbose_name_plural = "Customers"
