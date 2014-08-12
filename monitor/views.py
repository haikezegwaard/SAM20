from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from monitor.models import Project, Summary
from datetime import date, timedelta
from niki.nikiconverter import NikiConverter
from django.shortcuts import get_object_or_404


# Create your views here.

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project.html'


#create a new summary, store it and render result
class ProjectSummaryMail(generic.ListView):
    model = Summary
    template_name = 'summaryList.html'

    #def get_object(self):
    #    return Summary.objects.create(summary)

#view to fill the summaries
def summarize(request, projectId):
    summary = Summary()
    summary.project = get_object_or_404(Project, pk=projectId)
    now = date.today()
    summary.dateStart = now - timedelta(days=7)
    summary.dateEnd = now
    nikiconverter = NikiConverter()
    availability = nikiconverter.getAvailability(summary.project.nikiProject)
    summary.housesForSaleOrRent = availability[0]
    summary.housesSoldOrRented = availability[1]
    summary.housesUnderOption = availability[2]
    Summary.save(summary);
    return HttpResponseRedirect(reverse('summary'))


