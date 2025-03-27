import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class TaskUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("task_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("task_updates", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.handle_task_update(data)

    @sync_to_async
    def handle_task_update(self, data):
        pass

    async def task_update(self, event):
        task_data = event['task']
        await self.send(text_data=json.dumps(task_data))