from django.urls import path
from .views import IndexView, RoomView

app_name = 'chat'

urlpatterns = [
    path('', IndexView.as_view(), name='chat:index'),
    path('chat/<str:name_room>', RoomView.as_view(), name='chat:room'),
]