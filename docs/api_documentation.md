# Documentation de l'API de Gestion de Tâches

## Introduction
Cette API permet de gérer des tâches, des utilisateurs et des catégories.

## Authentification
Toutes les routes nécessitent une authentification via Token ou Session.

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
