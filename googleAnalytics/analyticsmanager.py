from django.contrib.auth.models import User
import requests
import logging
import json


class AnalyticsManager:

    GA_URL = 'https://www.googleapis.com/analytics/v3/data/ga?'

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


    def reporting_API_call(self, viewid, start, end, metrics):
        """Generic method for API Calls to Reporting API
        Args:
            viewid: string, id of specific property
            start: string, startdate in format yyyy-mm-dd
            end: string, enddate in format yyyy-mm-dd
            metrics: list of strings, metrics to be fetched e.g. goalCompletionsAll, sessions
        Returns:
            json decoded http response
        """
        user = User.objects.get(username="haike") #this should not be static
        #get the oath2 token for user haike
        social = user.social_auth.get(provider='google-oauth2')
        url = self.GA_URL + 'ids=ga:{}&start-date={}&end-date={}'.format(viewid, start, end)
        for metric in metrics:
            url += '&metrics=ga:{}'.format(metric)
        logging.debug('calling url: '+url)
        response = requests.get(url,params={'access_token': social.extra_data['access_token']})

        logging.debug('response: '+response.content)
        return json.loads(response.content)