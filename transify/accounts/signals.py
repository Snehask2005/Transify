from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, CommuterProfile

@receiver(post_save, sender=User)
def create_commuter_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'client':  # Only for commuters
        CommuterProfile.objects.create(user=instance)
