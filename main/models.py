from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)
    #a specific id that is going to be passed to the link

    #NOTE: superuser username: sylvia. Password is as usual
