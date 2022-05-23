from rest_framework import serializers
from .models import *


class ChartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charts
        fields = ('id', 'title', 'create_date')


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__'


class ChartInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charts
        fields = '__all__'


class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = '__all__'


class RadioStationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioStations
        fields = '__all__'


class LikedSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedSongs
        fields = ('track',)


class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'
