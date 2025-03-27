import pytest
from django.urls import reverse, resolve
from tasks.views import TaskViewSet

@pytest.mark.django_db
class TestTaskUrls:
    def test_task_list_url(self):
        """
        Test de la résolution de l'URL de liste des tâches
        """
        url = reverse('task-list')
        assert url == '/api/v1/tasks/'
        
        # Vérification de la résolution de l'URL
        resolver = resolve(url)
        assert resolver.func.cls == TaskViewSet

    def test_task_detail_url(self):
        """
        Test de la résolution de l'URL de détail d'une tâche
        """
        task_id = 1
        url = reverse('task-detail', kwargs={'pk': task_id})
        assert url == f'/api/v1/tasks/{task_id}/'
        
        # Vérification de la résolution de l'URL
        resolver = resolve(url)
        assert resolver.func.cls == TaskViewSet

    def test_create_task_url(self):
        """
        Test de la résolution de l'URL de création de tâche
        """
        url = reverse('task-list')
        resolver = resolve(url)
        assert hasattr(resolver.func.cls, 'create')

    def test_update_task_url(self):
        """
        Test de la résolution de l'URL de mise à jour de tâche
        """
        task_id = 1
        url = reverse('task-detail', kwargs={'pk': task_id})
        resolver = resolve(url)
        assert hasattr(resolver.func.cls, 'update')