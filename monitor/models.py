from django.db import models
from nikiInterest.models import InterestAccount

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 400)
    manager = models.CharField(max_length = 400)
    email = models.EmailField()
    url = models.URLField()
    nikiProject = models.CharField(max_length = 1000)
    ga_view = models.CharField(max_length = 1000)
    mailchimp_list_id = models.CharField(max_length = 1000)
    mailchimp_api_token = models.CharField(max_length = 1000)
    fanpage_id = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.name;

#Account for SOAP interest service
class InterestProject(models.Model):
    project = models.ForeignKey(Project)
    nikiProjectId = models.CharField(max_length = 400)
    interestAccount = models.ForeignKey(InterestAccount)


#Periodic summary
class Summary(models.Model):
    project = models.ForeignKey(Project)
    #cummulative values
    housesForSaleOrRent = models.IntegerField(max_length = 10)
    housesUnderOption = models.IntegerField(max_length = 10)
    housesSoldOrRented = models.IntegerField(max_length = 10)

    cummulativeInterest = models.IntegerField(max_length = 10)
    interest = models.IntegerField(max_length = 10)

    dateStart = models.DateField()
    dateEnd = models.DateField()

    def __unicode__(self):
        return str(self.dateStart) + ' - ' + str(self.dateEnd)


