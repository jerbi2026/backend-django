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
git clone https://github.com/jerbi2026/backend-django.git
cd backend-django
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
└── task_management/   # Configurations
└── scripts/           # Commandes pour démarrer le projet 
```

## 🔐 Variables d'Environnement Importantes

| Variable | Description | Exemple |
|----------|-------------|---------|
| `SECRET_KEY` | Clé secrète Django | `django-insecure-...` |
| `DEBUG` | Mode débogage | `True` ou `False` |
| `DATABASE_URL` | URL de connexion à la base de données | `postgres://user:pass@localhost/db` |
| `REDIS_URL` | URL du serveur Redis | `redis://localhost:6379/0` |



# 🌐 Documentation des Endpoints de l'API

## 📦 Endpoints de Tâches (TaskViewSet)
Base URL: `/api/tasks/`

### Opérations CRUD
- `GET /` : Lister toutes les tâches
- `POST /` : Créer une nouvelle tâche
- `GET /{task_id}/` : Détails d'une tâche spécifique
- `PUT /{task_id}/` : Mettre à jour une tâche
- `DELETE /{task_id}/` : Supprimer une tâche

### Actions Personnalisées
- `POST /{task_id}/add_comment/` : Ajouter un commentaire à une tâche

## 👥 Endpoints Utilisateurs (UserViewSet)
Base URL: `/api/users/`

### Authentification et Profil
- `POST /register/` : Inscription d'un nouvel utilisateur
  - Requiert : username, email, password
  - Retourne : user_id, username, email

- `GET /profile/` : Récupérer le profil de l'utilisateur connecté
- `PUT /profile/` : Mettre à jour le profil de l'utilisateur
- `PATCH /profile/` : Mise à jour partielle du profil

## 📁 Endpoints de Catégories (CategoryViewSet)
Base URL: `/api/categories/`

### Opérations CRUD (Réservées aux administrateurs)
- `GET /` : Lister toutes les catégories
- `POST /` : Créer une nouvelle catégorie
- `GET /{category_id}/` : Détails d'une catégorie
- `PUT /{category_id}/` : Mettre à jour une catégorie
- `DELETE /{category_id}/` : Supprimer une catégorie

## 🚨 Endpoints de Priorités (PriorityViewSet)
Base URL: `/api/priorities/`

### Opérations CRUD (Réservées aux administrateurs)
- `GET /` : Lister toutes les priorités
- `POST /` : Créer une nouvelle priorité
- `GET /{priority_id}/` : Détails d'une priorité
- `PUT /{priority_id}/` : Mettre à jour une priorité
- `DELETE /{priority_id}/` : Supprimer une priorité

## 💬 Endpoints de Commentaires (CommentViewSet)
Base URL: `/api/comments/`

### Opérations CRUD
- `GET /` : Lister tous les commentaires
- `POST /` : Créer un nouveau commentaire
- `GET /{comment_id}/` : Détails d'un commentaire
- `PUT /{comment_id}/` : Mettre à jour un commentaire
- `DELETE /{comment_id}/` : Supprimer un commentaire

## 🔐 Permissions
- La plupart des endpoints nécessitent une authentification
- Les endpoints de catégories et priorités sont réservés aux administrateurs
- Les utilisateurs ne peuvent modifier que leurs propres ressources

## 📝 Notes
- Tous les endpoints retournent des réponses JSON
- Les erreurs de validation renverront un code 400
- L'authentification se fait via token ou session

