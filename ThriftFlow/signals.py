from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Profit,Saving

@receiver(post_save, sender=Profit)
def create_saving_from_profit(sender, instance, created, **kwargs):
    if created:
        Saving.objects.create(profit=instance)
    user = instance.investment.user,
    source_profit = instance,
    amount = instance.amount,