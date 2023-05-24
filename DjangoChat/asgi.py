
import os

from django.core.asgi import get_asgi_application

from channels.routing import URLRouter, ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChat.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )

})

app = application
