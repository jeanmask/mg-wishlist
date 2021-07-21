from django.db.models.manager import Manager


class CustomerManager(Manager):
    def email_exists(self, email: str) -> bool:
        return super().get_queryset().filter(email=email).exists()
