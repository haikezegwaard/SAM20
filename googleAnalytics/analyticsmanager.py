import urllib2
from django.contrib.auth.models import User
import requests
import logging

class AnalyticsManager:

    def getConversionCount(self, id, start, end):

        user = User.objects.get(username="haike")
        social = user.social_auth.get(provider='google-oauth2')
        url = 'https://www.googleapis.com/analytics/v3/data/ga?ids=ga:{}&start-date={}&end-date={}&metrics=ga:goalCompletionsAll'.format(id, start, end)
        response = requests.get(url,params={'access_token': social.extra_data['access_token']})
        logging.debug('acces token: '+social.extra_data['access_token'])
        return response.content