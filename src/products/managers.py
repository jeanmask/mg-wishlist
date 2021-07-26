import httpx
from django.conf import settings
from django.db.models import Manager


class ProductManager(Manager):
    def update_or_create_from_api(self, product_id: str):
        response = httpx.get(f"{settings.CHALLENGE_API_URL}/product/{product_id}/")

        response.raise_for_status()
        payload = response.json()
        id_ = payload.pop("id")
        obj, _ = self.update_or_create(id=id_, defaults=payload)

        return obj
