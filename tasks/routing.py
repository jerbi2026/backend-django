from django.urls import re_path
from .consumers import TaskUpdateConsumer

websocket_urlpatterns = [
    re_path(r'ws/tasks/updates/$', TaskUpdateConsumer.as_asgi()),
]