# Generated by Django 4.0.4 on 2022-05-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_albums_genres_podcasts_radiostations_tracks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='file',
            field=models.FileField(default=None, upload_to='tracks/'),
        ),
    ]