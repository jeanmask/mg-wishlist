import pytest
from django.core.validators import validate_email
from django.db.utils import IntegrityError
from customers.models import Customer


@pytest.mark.django_db
def test_customer_create(customer):
    obj = Customer.objects.create(**customer)
    assert obj.name == customer["name"]
    assert obj.email == customer["email"]


@pytest.mark.django_db
@pytest.mark.parametrize("field", ("name", "email"))
def test_customer_required_fields(customer, field):
    with pytest.raises(IntegrityError, match=f"customers_customer.{field}"):
        customer[field] = None
        Customer.objects.create(**customer)


@pytest.mark.django_db
def test_customer_unique_email(customer):
    Customer.objects.get_or_create(email=customer["email"], defaults=customer)
    with pytest.raises(IntegrityError, match="customers_customer.email"):
        Customer.objects.create(**customer)
