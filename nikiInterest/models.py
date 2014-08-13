from django.db import models


# Create your models here.
class InterestAccount(models.Model):
    username = models.CharField(max_length = 400)
    password = models.CharField(max_length = 400)
    lastUpdate = models.DateTimeField()

    def __unicode__(self):
        return self.username





