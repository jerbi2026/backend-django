from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task, Category, Priority, Comment

User = get_user_model()

class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpass123'
        )
        
        self.priority = Priority.objects.create(name='medium')
        
        self.category = Category.objects.create(name='Développement')

    def test_create_task(self):
        task = Task.objects.create(
            title='Test Task',
            description='Une tâche de test',
            user=self.user,
            priority=self.priority,
            category=self.category
        )
        
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.priority, self.priority)
        self.assertEqual(task.status, 'pending')

    def test_create_comment(self):
        task = Task.objects.create(
            title='Commentaire Task',
            user=self.user,
            priority=self.priority
        )
        
        comment = Comment.objects.create(
            text='Un commentaire de test',
            user=self.user,
            task=task
        )
        
        self.assertEqual(comment.text, 'Un commentaire de test')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.task, task)