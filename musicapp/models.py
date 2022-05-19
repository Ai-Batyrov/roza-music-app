from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='user/photo')
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Albums(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.title


class Genres(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tracks(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres)
    file = models.FileField(upload_to='tracks/', default=None)

    def __str__(self):
        return self.title


class Playlists(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Tracks)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Charts(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateField()
    tracks = models.ManyToManyField(Tracks)

    def __str__(self):
        return self.title


class RadioStations(models.Model):
    title = models.CharField(max_length=255)
    broadcast_url = models.URLField()

    def __str__(self):
        return self.title


class Podcasts(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class LikedSongs(models.Model):
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
