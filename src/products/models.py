from django.db import models
from django.db.models.fields import (
    CharField,
    DateTimeField,
    DecimalField,
    URLField,
    UUIDField,
)


class Product(models.Model):
    id = UUIDField(primary_key=True)

    title = CharField(max_length=255)
    image = URLField(blank=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    review_score = DecimalField(max_digits=7, decimal_places=6, null=True)

    _last_update = DateTimeField(auto_now=True, db_index=True, editable=False)
