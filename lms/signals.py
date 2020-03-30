from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import LibraryCard, Patron


@receiver(post_save, sender=Patron)
def create_library_card(sender, instance, created, **kwargs):
    if created:
        LibraryCard.objects.create(patron=instance)
