from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer


class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().cache()
    serializer_class = PlayerSerializer
