#!/bin/bash

# Activer l'environnement virtuel
source venv/bin/activate

# Mise à jour des dépendances
pip install -r requirements.txt

# Migrations
python manage.py makemigrations
python manage.py migrate

# Collecte des fichiers statiques
python manage.py collectstatic --noinput

# Redémarrer les services
sudo systemctl restart task_management
sudo systemctl restart nginx