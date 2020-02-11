from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
from .models import Player
from .serializers import PlayerSerializer


class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
