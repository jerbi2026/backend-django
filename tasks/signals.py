from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Task
import json

@receiver(post_save, sender=Task)
def task_created_or_updated(sender, instance, created, **kwargs):
    """
    Envoie une mise à jour via WebSocket lors de la création ou modification d'une tâche
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "task_updates",
        {
            "type": "task_update",
            "task": {
                "id": instance.id,
                "title": instance.title,
                "status": instance.status,
                "updated_at": instance.updated_at.isoformat()
            }
        }
    )

@receiver(post_delete, sender=Task)
def task_deleted(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "task_updates",
        {
            "type": "task_update",
            "task": {
                "id": instance.id,
                "action": "deleted"
            }
        }
    )