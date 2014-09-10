import json
import logging
import requests
import pprint

class FacebookManager:
    """
    Interface for accessing the Facebook Insights api
    """
    GRAPH_URL = 'https://graph.facebook.com/'
    APP_ID = '139198506112454'
    APP_SECRET = '8405354cb36bf27b6a60e0e1af56467e'
    TOKEN = 'CAABZBma2ClcYBAKxAIV3A4xfSkcfRcU6QPSLZCfN9nZCyxNtuLOHdHyFkSHYiCSN6MqYEgT3p0HFGYPAqnVegMkoHpEKluXGksZBHZAOeQnhHd7JpgqCP4OZCeU46Jv2NCPPqLo3M9Xtd7F48UShkLqvpoLHsNspSx3KDApWqzArQlTwaqEbI5PzBre03BEOpG9ZBXNZAtSc6jjcTyZBgWVsd'

    def get_likes_sex_age(self, page):
        """
        Return sex / age spread for likes of page
        """
        url = '{}{}/insights/page_fans_gender_age'.format(self.GRAPH_URL, page)
        result = self.do_request(url)
        data = result.get('data').pop().get('values')


        lastvalues = max(data,key=lambda item:item['end_time']) #compare based on EACH items 'end_time' field
        return lastvalues.get('value')


    def do_request(self, url):
        """
        Append access token to url, do request and return json
        """
        url += '?access_token={}'.format(self.TOKEN)
        logging.debug('requesting url: {}'.format(url))
        r = requests.get(url)
        return r.json()
