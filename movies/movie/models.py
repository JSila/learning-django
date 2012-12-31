from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    runtime = models.IntegerField()
    imdb_link = models.URLField()

    def __unicode__(self):
        return self.title