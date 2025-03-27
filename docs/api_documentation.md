# Documentation de l'API de Gestion de Tâches

## Introduction
Cette API permet de gérer des tâches, des utilisateurs et des catégories.

## Authentification
Toutes les routes nécessitent une authentification via Token ou Session.

### Endpoints Utilisateurs
- `POST /api/users/register/` - Inscription
- `GET /api/users/profile/` - Profil utilisateur
- `PUT /api/users/profile/` - Mise à jour du profil

### Endpoints Tâches
- `GET /api/tasks/` - Liste des tâches
- `POST /api/tasks/` - Créer une tâche
- `GET /api/tasks/{id}/` - Détails d'une tâche
- `PUT /api/tasks/{id}/` - Mettre à jour une tâche
- `DELETE /api/tasks/{id}/` - Supprimer une tâche

### Websocket
- `ws://localhost:8000/ws/tasks/updates/` - Mises à jour en temps réel