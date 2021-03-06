from django.shortcuts import render
from django.views.generic import TemplateView
from googleAnalytics.analyticsmanager import AnalyticsManager
from nikiInterest.interestmanager import InterestManager
from nikiInterest.models import InterestAccount
from datetime import date, datetime, timedelta
from niki.nikiconverter import NikiConverter
import xml.etree.ElementTree as ET
from monitor.models import Project
from facebook.fbmanager import FacebookManager
import logging
from mcapi.mailchimp_manager import MailchimpManager

class DirectTemplateView(TemplateView):
    """View to display template without model, adding context from parameters"""
    extra_context = None
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value

        return context

class DigestView(TemplateView):

    extra_context = None
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value

        #get testproject
        project = Project.objects.get(name = context['projectname'])
        context['project'] = project
        #for testing purpose add content directly to context
        ga_manager = AnalyticsManager()
        ga_view = project.ga_view
        visits = ga_manager.get_weekly_visits(ga_view, '2014-08-01', '2014-08-14')
        context['traffic'] = visits['rows']

        conversions = ga_manager.get_conversion_count_for_goal(ga_view, 1 ,'2014-08-01', '2014-08-14')
        context['conversions'] = conversions
        conversion_rate = ga_manager.get_conversion_rate_for_goal(ga_view, 1, '2014-08-01', '2014-08-14')
        previous_conversion_rate = ga_manager.get_conversion_rate_for_goal(ga_view, 1, '2014-07-14', '2014-07-30')
        context['conversionrate'] = conversion_rate
        context['previousconversionrate'] = previous_conversion_rate
        interestManager = InterestManager()
        account = InterestAccount.objects.get(username='interessetester')
        projectId = '36002'
        start = datetime.today() - timedelta(days=360)
        idlist = interestManager.getIdsByProjectFrom(account, projectId, start)
        context['interest'] = len(idlist)

        nikimanager = NikiConverter()
        context['availability'] = nikimanager.getAvailability(project.nikiProject)

        #Get the sex and age spread of likes on the fanpage
        fbmanager = FacebookManager()
        agesexspread = fbmanager.get_likes_sex_age_spread_sorted('217907011622497')
        context['fbagesexspread'] = agesexspread


        #Get Mailchimp list growth statistics
        mcmanager = MailchimpManager(project.mailchimp_api_token)
        context['mailchimp'] = mcmanager.get_list_growth_data(project.mailchimp_list_id)

        return context





