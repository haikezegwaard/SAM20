from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from monitor.models import Project, Summary
from datetime import date, timedelta, datetime
from niki.nikiconverter import NikiConverter
from nikiInterest import interestmanager
from django.shortcuts import get_object_or_404
from nikiInterest.models import InterestAccount
from googleAnalytics.analyticsmanager import AnalyticsManager

# Create your views here.

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project.html'


#create a new summary, store it and render result
class ProjectSummaryMail(generic.ListView):
    model = Summary
    template_name = 'summaryList.html'


class ProfileView(generic.TemplateView):

    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProfileView,self).get_context_data(**kwargs)
        analyticsManager = AnalyticsManager()
        context['ga'] = analyticsManager.get_conversion_count('67007798', '2013-01-01', '2014-08-13')
        return context


#view to fill the summaries
def summarize(request, projectId):
    summary = Summary()
    summary.project = get_object_or_404(Project, pk=projectId)
    now = date.today()
    summary.dateStart = now - timedelta(days=7)
    summary.dateEnd = now
    #Get sale info from Niki REST API
    nikiconverter = NikiConverter()
    availability = nikiconverter.getAvailability(summary.project.nikiProject)
    summary.housesForSaleOrRent = availability[0]
    summary.housesSoldOrRented = availability[1]
    summary.housesUnderOption = availability[2]

    #GET interest info from Niki Interest API
    interestManager = interestmanager()
    projectId = '36002'
    account = InterestAccount.objects.get(username = "interessetester")
    interestStart = datetime.combine(summary.dateStart, datetime.min.time())
    summary.interest = len(interestManager.getIdsByProjectFrom(account, projectId, interestStart))
    summary.cummulativeInterest = len(interestManager.getIdsByProject(account, projectId))



    Summary.save(summary);
    return HttpResponseRedirect(reverse('summary'))


