from random import choice

import pytest

from customers.models import Customer


@pytest.fixture
def customers():
    return [
        {"name": "Dino da Silva Sauro", "email": "dino@fd.com"},
        {"name": "Bob da Silva Sauro", "email": "bob@fd.com"},
        {"name": "Charlene da Silva Sauro", "email": "charlene@fd.com"},
    ]


@pytest.fixture
def customer(customers):
    return choice(customers)
