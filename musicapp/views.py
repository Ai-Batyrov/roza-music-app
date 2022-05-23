from django.contrib.auth import login, logout
from django.contrib.auth.views import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .forms import *
from .utils import *


class HomeView(DataMixin, ListView):
    model = Tracks
    template_name = 'musicapp/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='roza')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'musicapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='roza - Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'musicapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='roza - Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def upload(request):
    successful = False
    if request.method == 'POST':
        form = UploadTracks(request.POST, request.FILES)
        if form.is_valid():
            successful = True
            form.save()

    else:
        form = UploadTracks()

    context = {
        'title': 'roza - Upload',
        'header_menu': header_menu,
        'form': form,
        'upload_message': successful
    }
    return render(request, 'musicapp/upload.html', context=context)


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


class GetAllTracksAPIView(generics.ListAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer


class GetPlaylistAPIView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'playlist_id'
    queryset = Playlists.objects.all()
    serializer_class = PlaylistsSerializer


class InsertLikedSongAPIView(generics.CreateAPIView):
    queryset = LikedSongs.objects.all()
    serializer_class = LikedSongsSerializer
    permission_classes = (IsAuthenticated,)
