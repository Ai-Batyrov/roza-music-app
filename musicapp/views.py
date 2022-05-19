from django.shortcuts import render
from rest_framework import generics

from musicapp.models import *
from musicapp.serializers import *


class ChartsAPIView(generics.ListAPIView):
    queryset = Charts.objects.all()
    serializer_class = ChartsSerializer


class PlaylistsAPIView(generics.ListAPIView):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistsSerializer
