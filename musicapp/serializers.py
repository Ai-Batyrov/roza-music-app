from rest_framework import serializers
from .models import *


class ChartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charts
        fields = '__all__'


class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = ('id', 'title')
