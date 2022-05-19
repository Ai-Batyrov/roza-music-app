from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'photo']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Albums)
admin.site.register(Charts)
admin.site.register(Genres)
admin.site.register(Tracks)
admin.site.register(Playlists)
admin.site.register(RadioStations)
admin.site.register(Podcasts)
admin.site.register(LikedSongs)
