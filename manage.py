#!/usr/bin/env python
"""
Script de gestion principal pour le projet Task Management.
Permet d'exécuter diverses commandes Django.
"""
import os
import sys

def main():
    """Execute les commandes de gestion Django."""
    # Définir le module des paramètres Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible de charger Django. Vérifiez que Django est installé "
            "et que votre environnement virtuel est activé."
        ) from exc
    
    # Ajout de chemins personnalisés si nécessaire
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Configuration pour la détection des tests
    import dotenv
    dotenv.load_dotenv()
    
    # Activation du mode débogage pour les tests
    if 'test' in sys.argv:
        os.environ.setdefault('DEBUG', 'True')
    
    main()