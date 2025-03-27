import logging
import uuid

def generate_unique_id():
    """
    Génère un identifiant unique universel
    """
    return str(uuid.uuid4())

def get_logger(name):
    """
    Retourne un logger configuré
    """
    return logging.getLogger(name)

def log_task_event(logger, event_type, task_id, user_id=None):
    """
    Enregistre un événement lié aux tâches
    """
    extra = {
        'task_id': task_id,
        'user_id': user_id
    }
    logger.info(f"Task {event_type}: {task_id}", extra=extra)