from ninja.schema import Schema
from pydantic import UUID4, EmailStr, Field, constr

__all__ = ["CustomerOut", "CustomerIn"]


class CustomerOut(Schema):
    id: UUID4 = Field(descripion="Customer UUID4 identifier")
    name: str = Field(descripion="Customer fullname")
    email: EmailStr = Field(descripion="Customer unique email address")


class CustomerIn(Schema):
    name: constr(min_length=1, max_length=255) = Field(descripion="Customer fullname")
    email: EmailStr = Field(descripion="Customer unique email address")
