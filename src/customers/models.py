import uuid

from django.db import models
from django.db.models.fields import CharField, EmailField, UUIDField

from .managers import CustomerManager


class Customer(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Customer UUID")
    name = CharField(blank=False, max_length=255, help_text="Customer name")
    email = EmailField(blank=False, unique=True, help_text="Customer unique email address")

    objects = CustomerManager()

    def __repr__(self):
        return f"{self.name} <{self.email}>"

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    class Meta:
        unique_together = (("customer", "product"),)
