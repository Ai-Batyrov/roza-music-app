from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from musicapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/v1/charts/', ChartsAPIView.as_view(), name='charts'),
    path('api/v1/chart/<int:chart_id>', TracksInChartAPIView.as_view(), name='get-tracks-in-chart'),
    path('api/v1/track/<int:track_id>', TrackAPIView.as_view(), name='get-tracks'),
    path('api/v1/playlists/', PlaylistsAPIView.as_view(), name='playlists-view'),
    path('api/v1/radiostations/', RadioStationsAPIView.as_view(), name='radio-stations-view'),
    path('api/v1/radiostation/<int:radio_id>', RadioAPIView.as_view(), name='get-radio'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
