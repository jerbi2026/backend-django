import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible de charger Django. Vérifiez que Django est installé "
            "et que votre environnement virtuel est activé."
        ) from exc
    
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    import dotenv
    dotenv.load_dotenv()
    
    if 'test' in sys.argv:
        os.environ.setdefault('DEBUG', 'True')
    
    main()