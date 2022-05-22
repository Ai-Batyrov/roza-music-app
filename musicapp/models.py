from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


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
    # cover = models.ImageField(upload_to='covers/',
    #                           default='https://i.pinimg.com/564x/63/77/b9/6377b973d63f875455b450361e6c13fd.jpg')
    file = models.FileField(upload_to='tracks/', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'get-tracks',
            kwargs={'track_id': self.pk}
        )


class Playlists(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Tracks)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Charts(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateField(auto_now=True)
    tracks = models.ManyToManyField(Tracks)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'get-tracks-in-chart',
            kwargs={'chart_id': self.pk}
        )


class RadioStations(models.Model):
    title = models.CharField(max_length=255)
    broadcast_url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get-radio', kwargs={'radio_id': self.pk})


class Podcasts(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class LikedSongs(models.Model):
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.track) + ' - ' + str(self.user)
