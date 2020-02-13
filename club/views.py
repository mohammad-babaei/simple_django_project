from rest_framework import viewsets
from .serializers import ClubSerializer
from .models import Club


class ClubModelViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all().cache()
