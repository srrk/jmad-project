from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Solo(models.Model):
    track = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    album = models.CharField(max_length=200)
    start_time = models.CharField(max_length=20, blank=True,
            null=True)
    end_time = models.CharField(max_length=20, blank=True,
            null=True)

    def get_absolute_url(self):
        return reverse('solo_detail_view', kwargs={
            'album' : self.track.album.slug,
            'track' : self.track.slug,
            'artist' : self.slug
        })
