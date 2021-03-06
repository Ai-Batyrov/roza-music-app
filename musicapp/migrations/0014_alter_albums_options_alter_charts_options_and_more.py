# Generated by Django 4.0.4 on 2022-05-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0013_remove_tracks_genres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albums',
            options={'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterModelOptions(
            name='charts',
            options={'verbose_name': 'Chart', 'verbose_name_plural': 'Charts'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='likedsongs',
            options={'verbose_name': 'LikedSong', 'verbose_name_plural': 'LikedSongs'},
        ),
        migrations.AlterModelOptions(
            name='playlists',
            options={'verbose_name': 'Playlist', 'verbose_name_plural': 'Playlists'},
        ),
        migrations.AlterModelOptions(
            name='podcasts',
            options={'verbose_name': 'Podcast', 'verbose_name_plural': 'Podcasts'},
        ),
        migrations.AlterModelOptions(
            name='radiostations',
            options={'verbose_name': 'RadioStation', 'verbose_name_plural': 'RadioStations'},
        ),
        migrations.AlterModelOptions(
            name='tracks',
            options={'verbose_name': 'Track', 'verbose_name_plural': 'Tracks'},
        ),
        migrations.AddField(
            model_name='charts',
            name='cover',
            field=models.ImageField(default=None, upload_to='charts/covers'),
            preserve_default=False,
        ),
    ]
