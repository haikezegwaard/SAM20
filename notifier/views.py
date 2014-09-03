from django.shortcuts import render
from django.views.generic import TemplateView
from googleAnalytics.analyticsmanager import AnalyticsManager

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

        #for testing purpose add content directly to context
        ga_manager = AnalyticsManager()
        visits = ga_manager.get_weekly_visits('67007798', '2014-08-01', '2014-08-07')
        context['traffic'] = visits['rows']


        return context



