from django.urls import path

from .views import rooms, room

app_name = 'room'

urlpatterns = [
    path('', rooms, name='rooms'),
    path('<slug:slug>/', room, name='room'),
]
