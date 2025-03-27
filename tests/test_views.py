import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task, Category, Priority
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestTaskViews:
    def setup_method(self):
        """
        Configuration initiale pour chaque test
        """
        self.client = APIClient()
        
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )
        
        # Création de catégories et priorités de test
        self.category = Category.objects.create(name='Développement')
        self.priority = Priority.objects.create(name='high')
        
        # Authentification du client
        self.client.force_authenticate(user=self.user)
        
        # Création de tâches de test
        self.task_data = {
            'title': 'Tâche de Test',
            'description': 'Description de la tâche de test',
            'category': self.category,
            'priority': self.priority,
            'user': self.user
        }
        self.task = Task.objects.create(**self.task_data)

    def test_create_task(self):
        """
        Test de création d'une nouvelle tâche
        """
        url = reverse('task-list')
        new_task_data = {
            'title': 'Nouvelle Tâche',
            'description': 'Description de la nouvelle tâche',
            'category': self.category.id,
            'priority': self.priority.id
        }
        
        response = self.client.post(url, new_task_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == new_task_data['title']

    def test_list_tasks(self):
        """
        Test de listing des tâches
        """
        url = reverse('task-list')
        response = self.client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) > 0

    def test_update_task(self):
        """
        Test de mise à jour d'une tâche
        """
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        update_data = {
            'title': 'Tâche Mise à Jour',
            'description': 'Description mise à jour'
        }
        
        response = self.client.patch(url, update_data)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == update_data['title']

    def test_delete_task(self):
        """
        Test de suppression d'une tâche
        """
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.delete(url)
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Task.objects.filter(id=self.task.id).exists()