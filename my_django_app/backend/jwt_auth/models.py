# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    # custom fields here...
    image = models.CharField(max_length=200)

    # could add favourites in customer user model