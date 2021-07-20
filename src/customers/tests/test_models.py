import pytest
from django.core.validators import validate_email

from customers.models import Customer


@pytest.mark.django_db
def test_customer_create(customer):
    obj = Customer.objects.create(**customer)
    assert obj.name == customer["name"]
    assert obj.email == customer["email"]
    assert validate_email(obj.email) is None, "Customer email must be a valid email"
