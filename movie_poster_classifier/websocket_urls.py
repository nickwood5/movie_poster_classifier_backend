from django.urls import path
from movie_poster_classifier.views.websocket.ping_consumer import PingConsumer

websocket_urlpatterns = [
    path("api/ws/ping/", PingConsumer.as_asgi()),
]
