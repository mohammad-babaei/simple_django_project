from rest_framework import serializers
from .models import Player
from club.serializers import ClubSerializer
from club.models import Club


class PlayerSerializer(serializers.ModelSerializer):
    club = serializers.HyperlinkedRelatedField(
        view_name='club-detail',
        queryset=Club.objects.all(),
    )

    class Meta:
        model = Player
        fields = '__all__'
