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

#Account for SOAP interest service
class InterestAccount(models.Model):
    project = models.ForeignKey(Project)
    username = models.CharField(max_length = 400)
    password = models.CharField(max_length = 400)
    nikiProjectId = models.CharField(max_length = 400)

#Periodic summary
class Summary(models.Model):
    project = models.ForeignKey(Project)
    #cummulative values
    housesForSaleOrRent = models.IntegerField(max_length = 10)
    housesUnderOption = models.IntegerField(max_length = 10)
    housesSoldOrRented = models.IntegerField(max_length = 10)

    dateStart = models.DateField()
    dateEnd = models.DateField()

    def __unicode__(self):
        return str(self.dateStart) + ' - ' + str(self.dateEnd)

class InterestCount(models.Model):
    project

class HouseTypeCount(models.Model):
    project = models.ForeignKey

