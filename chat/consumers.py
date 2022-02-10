from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # Enter the chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, code):
        # leave the chat
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    # receive message from websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # send the message to the chat
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        
    # receive message of the chat
    async def chat_message(self, event):
        message = event['message']
        
        # send the message for the websocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
             