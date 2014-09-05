from django.contrib.auth.models import User
import requests
import logging
import json


class AnalyticsManager:

    GA_URL = 'https://www.googleapis.com/analytics/v3/data/ga?'

    def get_weekly_visits(self, viewid, start, end):
        """For convenience only"""
        return self.reporting_API_call(viewid, start, end, ['sessions','pageviews'], '&sort=ga:date&dimensions=ga:date&max-results=200')

    def get_conversion_count(self, viewid, start, end):
        """Get conversion count for specific view id in daterange
        Args:
            viewid: string, id of specific property
            start: string, startdate in format yyyy-mm-dd
            end: string, enddate in format yyyy-mm-dd
        Returns:
            int, number of goal completions
        """
        obj = self.reporting_API_call(viewid, start, end, ['goalCompletionsAll'])
        return int(obj['totalsForAllResults']['ga:goalCompletionsAll']);


    def get_conversion_count_for_goal(self, viewid, goalid, start, end):
        """Get conversion count for specific view id and specific goal number in daterange
        Args:
            viewid: string, id of specific property
            goalid: id of specific goal
            start: string, startdate in format yyyy-mm-dd
            end: string, enddate in format yyyy-mm-dd
        Returns:
            int, number of goal completions
        """
        action = 'goal{}Completions'.format(goalid)
        obj = self.reporting_API_call(viewid, start, end, [action])
        return int(obj['totalsForAllResults']['ga:'+action]);


    def get_conversion_rate_for_goal(self, viewid, goalid, start, end):
        """Get conversion rate for specific view id and specific goal number in daterange
        Args:
            viewid: string, id of specific property
            goalid: id of specific goal
            start: string, startdate in format yyyy-mm-dd
            end: string, enddate in format yyyy-mm-dd
        Returns:
            perc, goal gonversion rate
        """
        action = 'goal{}ConversionRate'.format(goalid)
        obj = self.reporting_API_call(viewid, start, end, [action])
        return round(float(obj['totalsForAllResults']['ga:'+action]),2);


    def get_session_count(self, viewid, start, end):
        """Get session count for specific view id in daterange
        Args:
            viewid: string, id of specific property
            start: string, startdate in format yyyy-mm-dd
            end: string, enddate in format yyyy-mm-dd
        Returns:
            int, number of sessions
        """
        obj = self.reporting_API_call(viewid, start, end, ['sessions'])
        return int(obj['totalsForAllResults']['ga:sessions'])


    def reporting_API_call(self, viewid, start, end, metrics, extra = ''):
        """Generic method for API Calls to Reporting API
        Args:
            viewid: string, id of specific property
            start: string, startdate in format yyyy-mm-dd
            end: string, enddate in format yyyy-mm-dd
            metrics: list of strings, metrics to be fetched e.g. goalCompletionsAll, sessions
            extra: string to append to the query-url
        Returns:
            json decoded http response
        """
        user = User.objects.get(username="haike") #this should not be static
        #get the oath2 token for user haike
        social = user.social_auth.get(provider='google-oauth2')
        url = self.GA_URL + 'ids=ga:{}&start-date={}&end-date={}'.format(viewid, start, end)
        url += '&metrics='
        for metric in metrics:
            url += 'ga:{},'.format(metric)
        url = url[:-1]
        url += extra
        logging.debug('calling url: '+url)
        response = requests.get(url,params={'access_token': social.extra_data['access_token']})

        logging.debug('response: '+response.content)
        return json.loads(response.content)