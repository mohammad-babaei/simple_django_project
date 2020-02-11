from rest_framework import routers
from .views import PlayerModelViewSet

player_router = routers.SimpleRouter()
player_router.register(r'players', PlayerModelViewSet)
