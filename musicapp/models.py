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

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'


class Genres(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Tracks(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/')
    file = models.FileField(upload_to='tracks/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'get-tracks',
            kwargs={'track_id': self.pk}
        )

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'


class Playlists(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Tracks)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'


class Charts(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateField(auto_now=True)
    cover = models.ImageField(upload_to='charts/covers')
    tracks = models.ManyToManyField(Tracks)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'get-tracks-in-chart',
            kwargs={'chart_id': self.pk}
        )

    class Meta:
        verbose_name = 'Chart'
        verbose_name_plural = 'Charts'


class RadioStations(models.Model):
    title = models.CharField(max_length=255)
    broadcast_url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get-radio', kwargs={'radio_id': self.pk})

    class Meta:
        verbose_name = 'RadioStation'
        verbose_name_plural = 'RadioStations'


class Podcasts(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcasts'


class LikedSongs(models.Model):
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.track) + ' - ' + str(self.user)

    class Meta:
        verbose_name = 'LikedSong'
        verbose_name_plural = 'LikedSongs'
