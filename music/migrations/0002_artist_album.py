from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_remove_album_album_cover_alter_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]