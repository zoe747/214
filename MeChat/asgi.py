import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import infrastructure.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MeChat.settings")

application = ProtocolTypeRouter({
    # http请求使用这个
    "http": get_asgi_application(),

    # websocket请求使用这个
    "websocket": AuthMiddlewareStack(
        URLRouter(
            infrastructure.routing.websocket_urlpatterns
        )
    ),
})
