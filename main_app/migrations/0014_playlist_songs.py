# Generated by Django 4.1.3 on 2022-11-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_song_album_alter_song_composer'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='main_app.song'),
        ),
    ]