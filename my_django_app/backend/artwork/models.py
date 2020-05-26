from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=50)
  nationality = models.CharField(max_length=50)
  image = models.CharField(max_length=400)
  def __str__(self):
    return self.name

class Period(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Art(models.Model):
  # CharField (character filed). Give this a max length
    name = models.CharField(max_length=50)
    created = models.IntegerField()
    image = models.CharField(max_length=500)
    location = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, related_name='artworks', on_delete=models.CASCADE)
    period = models.ManyToManyField(Period, related_name='artworks', blank=True)
    user = models.ForeignKey(User, related_name='artworks', on_delete=models.CASCADE)

    # blank = true (means optional field)

    def __str__(self):
        return self.name
        