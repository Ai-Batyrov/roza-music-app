# Generated by Django 4.0.4 on 2022-05-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0008_alter_tracks_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers/'),
        ),
    ]