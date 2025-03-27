# Guide de Déploiement

## Prérequis
- Python 3.9+
- PostgreSQL
- Redis
- Gunicorn
- Nginx

## Étapes de Déploiement

### 1. Préparation de l'environnement
```bash
# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configuration de la base de données
- Créer une base de données PostgreSQL
- Mettre à jour les paramètres dans `.env`

### 3. Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Collecte des fichiers statiques
```bash
python manage.py collectstatic
```

### 5. Configuration Gunicorn
```bash
gunicorn task_management.wsgi:application \
    --workers 3 \
    --bind unix:/run/task_management.sock
```

### 6. Configuration Nginx
Voir exemple de configuration dans `deployment/nginx.conf`

### 7. Sécurité
- Générer une nouvelle `SECRET_KEY`
- Désactiver `DEBUG`
- Configurer `ALLOWED_HOSTS`