from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Checkout, CheckoutHistory, LibraryCard, Patron


@receiver(post_save, sender=Patron)
def create_library_card(sender, instance, created, **kwargs):
    if created:
        LibraryCard.objects.create(patron=instance)


@receiver(post_save, sender=Checkout)
def create_checkout_history(sender, instance, created, **kwargs):
    if created:
        CheckoutHistory.objects.create(
            library_asset=instance.library_asset,
            library_card=instance.library_card
        )
