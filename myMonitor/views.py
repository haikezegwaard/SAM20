from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views import generic
from myMonitor.models import Project, Summary
from datetime import date, timedelta
from niki.nikiconverter import NikiConverter


# Create your views here.

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project.html'


#create a new summary, store it and render result
class ProjectSummaryMail(generic.DetailView):
    model = Project
    template_name = 'summary.html'

    def get_object(self):
        summary = Summary()
        summary.project = super(ProjectSummaryMail, self).get_object()
        now = date()
        summary.dateStart = now - timedelta(days=7)
        summary.dateEnd = now
        nikiconverter = NikiConverter()
        summary.housesForSaleOrRent = nikiconverter.getHousesForSaleOrRent(summary.project.nikiProject)
        summary.housesSoldOrRented = nikiconverter.getHousesSoldOrRented(summary.project.nikiProject)
        summary.housesUnderOption = nikiconverter.getHousesUnderOption(summary.project.nikiProject)

        return Summary.objects.create(summary)


