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

#Periodic summary
class Summary(models.Model):
    project = models.ForeignKey(Project)
    housesForSaleOrRent = models.IntegerField(max_length = 10)
    housesUnderOption = models.IntegerField(max_length = 10)
    housesSoldOrRented = models.IntegerField(max_length = 10)
    dateStart = models.DateField()
    dateEnd = models.DateField()



