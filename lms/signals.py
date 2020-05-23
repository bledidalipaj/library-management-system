from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils import timezone

from .enums import StatusEnum
from .models import Checkout, CheckoutHistory, Hold, LibraryCard, Patron, Status


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


@receiver(post_save, sender=Checkout)
def update_library_asset_status_post_save(sender, instance, created, **kwargs):
    library_asset = instance.library_asset

    if created:
        if not library_asset.is_available_to_borrow:
            updated_status = Status.objects.get(
                name=StatusEnum.CHECKED_OUT.value)
            library_asset.status = updated_status
            library_asset.save()


@receiver(post_delete, sender=Checkout)
def update_library_asset_status_post_delete(sender, instance, **kwargs):
    library_asset = instance.library_asset
    library_card = instance.library_card

    checkout_history_entry = get_list_or_404(
        CheckoutHistory, library_asset=library_asset, library_card=library_card)[0]
    checkout_history_entry.checked_in = timezone.now()
    checkout_history_entry.save()

    # checkout asset to the patron that has placed the first hold
    holds = Hold.objects.filter(library_asset=library_asset)

    if holds:
        for hold in holds:
            if hold.library_card.can_borrow:
                Checkout.objects.create(
                    library_asset=library_asset,
                    library_card=hold.library_card
                )
                hold.delete()
                break

    if library_asset.is_available_to_borrow:
        updated_status = Status.objects.get(name=StatusEnum.AVAILABLE.value)
        library_asset.status = updated_status
        library_asset.save()
