from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja.errors import ValidationError
from ninja.security import HttpBearer

from products.models import Product

from .models import Customer, Wishlist
from .schemas import CustomerIn, CustomerOut, ProductWishlistIn, ProductWishlistOut


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


api = NinjaAPI(title="Wishlist API", auth=AuthBearer())


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


@api.get("/{customer_id}/wishlist", response={200: List[ProductWishlistOut]})
def list_customer_wishlist(request, customer_id: str):
    customer = get_object_or_404(Customer, id=customer_id)
    return customer.wishlist.values()


@api.post("/{customer_id}/wishlist", response={201: None})
def add_customer_wishlist_item(request, customer_id: str, payload: ProductWishlistIn):
    customer = get_object_or_404(Customer, id=customer_id)

    if customer.wishlist.filter(id=payload.product_id).exists():
        raise ValidationError(f"Product <{payload.product_id}> already exists in wishlist")

    product_obj = Product.objects.update_or_create_from_api(payload.product_id)

    customer.wishlist.add(product_obj)

    return 201, None


@api.delete("/{customer_id}/wishlist", response={204: None})
def remove_customer_wishlist_item(request, customer_id: str, payload: ProductWishlistIn):
    customer = get_object_or_404(Wishlist, customer_id=customer_id, product_id=payload.product_id)
    customer.delete()

    return 204, None
