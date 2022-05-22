from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class ChartsAPIView(generics.ListAPIView):
    queryset = Charts.objects.all()
    serializer_class = ChartsSerializer


class TracksInChartAPIView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'chart_id'
    queryset = Charts.objects.all()
    serializer_class = ChartInstanceSerializer


class TrackAPIView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'track_id'
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer


class PlaylistsAPIView(generics.ListAPIView):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistsSerializer


class RadioStationsAPIView(generics.ListAPIView):
    queryset = RadioStations.objects.all()
    serializer_class = RadioStationsSerializer


class RadioAPIView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'radio_id'
    queryset = RadioStations.objects.all()
    serializer_class = RadioStationsSerializer


class LikedSongsAPIView(generics.ListAPIView):
    queryset = LikedSongs.objects.filter(user_id__exact=1)
    serializer_class = LikedSongsSerializer


class SearchAPIView(generics.ListAPIView):
    serializer_class = TracksSerializer

    def get_queryset(self):
        title = self.kwargs['text']
        return Tracks.objects.filter(title__exact=title)
