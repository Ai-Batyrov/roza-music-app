from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from musicapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('upload/', upload, name='upload-track'),
    path('api/v1/charts/', ChartsAPIView.as_view(), name='charts'),
    path('api/v1/chart/<int:chart_id>', TracksInChartAPIView.as_view(), name='get-tracks-in-chart'),
    path('api/v1/track/<int:track_id>', TrackAPIView.as_view(), name='get-tracks'),
    path('api/v1/playlists/', PlaylistsAPIView.as_view(), name='playlists-view'),
    path('api/v1/radiostations/', RadioStationsAPIView.as_view(), name='radio-stations-view'),
    path('api/v1/radiostation/<int:radio_id>', RadioAPIView.as_view(), name='get-radio'),
    path('api/v1/likedsongs/', LikedSongsAPIView.as_view(), name='get-liked-songs'),
    path('api/v1/search/<str:text>', SearchAPIView.as_view(), name='search-result'),
    path('api/v1/get/all-tracks', GetAllTracksAPIView.as_view(), name='get-all-tracks'),
    path('api/v1/get/playlist/<int:playlist_id>', GetPlaylistAPIView.as_view(), name='get-playlist'),
    path('api/v1/post/liked-songs/<int:track_id>', InsertLikedSongAPIView.as_view(), name='post-liked-track'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
