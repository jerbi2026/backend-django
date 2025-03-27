import os
from django.core.wsgi import get_wsgi_application

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')

# Obtention de l'application WSGI
application = get_wsgi_application()