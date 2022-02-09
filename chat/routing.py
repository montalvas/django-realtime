from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlspatterns = [
    re_path(r'ws/chat/(?P<name_room>\w+)/$', ChatConsumer),
]
