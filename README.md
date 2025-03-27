# Système de Gestion de Tâches - Backend Django

## 🚀 Présentation du Projet

Ce projet est un système complet de gestion de tâches développé avec Django, offrant des fonctionnalités avancées de suivi, de collaboration et de productivité.

## 📋 Fonctionnalités Principales

- Gestion complète des tâches
- Authentification utilisateur
- Filtrage et recherche avancés
- Mises à jour en temps réel via WebSockets
- API RESTful complète
- Gestion des erreurs et logging structuré

## 🛠 Prérequis Techniques

- Python 3.9+
- pip
- virtualenv
- PostgreSQL
- Redis (pour WebSockets)

## 🔧 Installation et Configuration

### 1. Clonage du Projet

```bash
git clone https://github.com/votre-utilisateur/task-management-backend.git
cd task-management-backend
```

### 2. Configuration de l'Environnement Virtuel

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Unix/macOS
source venv/bin/activate

# Sur Windows
venv\Scripts\activate
```

### 3. Installation des Dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration de la Base de Données

1. Créer un fichier `.env` à la racine du projet avec les configurations suivantes :

```env
SECRET_KEY=votre_clé_secrète
DEBUG=True
DATABASE_URL=postgres://utilisateur:motdepasse@localhost/task_management
REDIS_URL=redis://localhost:6379/0
```

2. Créer la base de données PostgreSQL
```bash
createdb task_management
```

### 5. Migrations et Initialisation

```bash
# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser
```

## 🚀 Lancement du Projet

### Serveur de Développement

```bash
# Lancer le serveur Django
python manage.py runserver

# Lancer le serveur WebSocket
daphne task_management.asgi:application
```

### Serveur de Production

```bash
# Collecte des fichiers statiques
python manage.py collectstatic

# Lancement avec Gunicorn
gunicorn --worker-class channels.routing.ChannelsWorker task_management.asgi:application
```

## 🧪 Tests

```bash
# Exécuter tous les tests
pytest

# Vérification de la couverture des tests
pytest --cov=tasks
```

## 📦 Structure du Projet

```
task_management_project/
├── manage.py
├── requirements.txt
├── tasks/             # Logique des tâches
├── users/             # Gestion des utilisateurs
├── core/              # Utilitaires partagés
├── tests/             # Tests unitaires et d'intégration
└── docs/              # Documentation
```

## 🔐 Variables d'Environnement Importantes

| Variable | Description | Exemple |
|----------|-------------|---------|
| `SECRET_KEY` | Clé secrète Django | `django-insecure-...` |
| `DEBUG` | Mode débogage | `True` ou `False` |
| `DATABASE_URL` | URL de connexion à la base de données | `postgres://user:pass@localhost/db` |
| `REDIS_URL` | URL du serveur Redis | `redis://localhost:6379/0` |

## 🔒 Bonnes Pratiques de Sécurité

- Ne partagez jamais votre fichier `.env`
- Utilisez des mots de passe forts
- Activez l'authentification à deux facteurs
- Maintenez vos dépendances à jour

## 🤝 Contribution

1. Forker le projet
2. Créer une branche de fonctionnalité
3. Commiter vos modifications
4. Créer une Pull Request

## 📄 Licence

[Spécifier votre licence]

## 📞 Support

En cas de problème, veuillez ouvrir un ticket GitHub ou contacter l'équipe de développement.
```

Maintenant, je vais vous donner un script shell pour faciliter le lancement du projet :

<antArtifact identifier="project-launcher" type="application/vnd.ant.code" language="bash" title="Script de Lancement du Projet">
#!/bin/bash

# Script de lancement du projet Django Task Management

# Couleurs pour les messages
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonction pour afficher un message
print_message() {
    echo -e "${GREEN}[TASK MANAGEMENT]${NC} $1"
}

# Vérifier si l'environnement virtuel est activé
check_venv() {
    if [ -z "$VIRTUAL_ENV" ]; then
        print_message "${YELLOW}ATTENTION: Environnement virtuel non activé !${NC}"
        print_message "Activez-le avec: source venv/bin/activate"
        exit 1
    fi
}

# Commande de lancement
start_project() {
    check_venv

    # Migrations
    print_message "Application des migrations..."
    python manage.py makemigrations
    python manage.py migrate

    # Démarrage des serveurs en parallèle
    print_message "Démarrage du serveur Django et WebSocket..."
    
    # Lance le serveur Django
    python manage.py runserver & 
    
    # Lance le serveur WebSocket
    daphne task_management.asgi:application &

    # Attendre que les processus se terminent
    wait
}

# Lancement des tests
run_tests() {
    check_venv
    print_message "Exécution des tests..."
    pytest
}

# Menu principal
main() {
    case "$1" in
        "start")
            start_project
            ;;
        "test")
            run_tests
            ;;
        *)
            echo "Usage: $0 {start|test}"
            exit 1
    esac
}

main "$@"
