from django.shortcuts import render
from django.views import generic
from nikiInterest.models import InterestAccount
from nikiInterest.InterestManager import InterestManager
from datetime import date, datetime, timedelta
import xml.etree.ElementTree as ET

# Create your views here.
# Create your views here.

class IndexView(generic.TemplateView):

    #model = InterestAccount
    template_name = 'nikiInterest/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView,self).get_context_data(**kwargs)

        start = datetime.today() - timedelta(days=14)

        # Add in a QuerySet of all the books
        interestManager = InterestManager()
        #context['myVar'] = interestManager.getSubscribersSinceDate(datetime(2014, 7, 29, 13, 1, 31))
        account = InterestAccount.objects.get(username='interessetester')
        #context['myVar'] = interestManager.getById(account, '171795')
        #context['myVar'] = interestManager.syncAllAccounts()
        projectId = '36002'
        idlist = interestManager.getIdsByProjectFrom(account, projectId, start)
        context['project_count'] = len(idlist)
        document = interestManager.getSubscriptionsAsDocument(account, idlist)
        context['alldoc'] = ET.tostring(document, encoding='utf8', method='xml')
        context['occurrences'] = interestManager.mapSubscriptionDocumentToTypCountDictionary(document)
        return context






