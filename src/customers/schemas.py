from typing import Optional

from ninja.schema import Schema
from pydantic import UUID4, EmailStr, Field, HttpUrl, condecimal, constr, validator

__all__ = ["CustomerOut", "CustomerIn"]


class CustomerOut(Schema):
    id: UUID4 = Field(descripion="Customer UUID4 identifier")
    name: str = Field(descripion="Customer fullname")
    email: EmailStr = Field(descripion="Customer unique email address")


class CustomerIn(Schema):
    name: constr(min_length=1, max_length=255) = Field(descripion="Customer fullname")
    email: EmailStr = Field(descripion="Customer unique email address")


class ProductWishlistIn(Schema):
    product_id: str = Field(description="Product UUID4 identifier")


class ProductWishlistOut(Schema):
    id: str = Field(description="Product identifier")
    title: str
    image: HttpUrl
    brand: str
    price: condecimal(max_digits=10, decimal_places=2)
    review_score: Optional[condecimal(max_digits=7, decimal_places=6)]

    @validator("id", pre=True)
    def parse_id(cls, v):
        return str(v)
