from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja.errors import ValidationError

from .models import Customer
from .schemas import CustomerIn, CustomerOut

api = NinjaAPI()


@api.get("/", response=List[CustomerOut])
def list_customers(request):
    customers = Customer.objects.all()

    return customers


@api.get("/{customer_id}", response={200: CustomerOut})
def get_customer(request, customer_id: str):
    customer = get_object_or_404(Customer, id=customer_id)

    return 200, customer


@api.post("/", response={201: CustomerOut})
def create_customer(request, payload: CustomerIn):
    if Customer.objects.email_exists(payload.email):
        raise ValidationError("Customer e-mail already exists")

    customer = Customer.objects.create(**payload.dict())

    return 201, customer


@api.put("/{customer_id}", response={200: CustomerOut})
def update_customer(request, customer_id: str, payload: CustomerIn):
    customer = get_object_or_404(Customer, id=customer_id)

    if customer.email != payload.email and Customer.objects.email_exists(payload.email):
        raise ValidationError("Customer e-mail already exists")

    for name, value in payload.dict().items():
        setattr(customer, name, value)

    customer.save()

    return 200, customer


@api.delete("/{customer_id}", response={204: None})
def delete_customer(request, customer_id: str):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()

    return 204, None
