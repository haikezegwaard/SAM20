from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 400)
    manager = models.CharField(max_length = 400)
    email = models.EmailField()
    url = models.URLField()
    nikiProject = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.name;



