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

    def get_likes_sex_age_spread_sorted(self, page):
        """
        Return age / sex spread formatted for use in Google Chart
        """
        agesexspread = self.get_likes_sex_age(page)
        fullspread = {}
        for k, v in agesexspread.items():
            if k.startswith('M.'):
                testkey = u'F.{}'.format(k[2:])
            if k.startswith('F.'):
                testkey = u'M.{}'.format(k[2:])
            if testkey not in agesexspread:
                fullspread[testkey] = 0
            fullspread[k] = v
        logging.debug(fullspread)

        male = {k[2:]: v for k, v in fullspread.items() if k.startswith('M.')}
        female = {k[2:]: v for k, v in fullspread.items() if k.startswith('F.')}

        d = {}
        for i in male.keys():
            d[i] = [male[i], female[i]]

        return (sorted(d.items()))


    def do_request(self, url):
        """
        Append access token to url, do request and return json
        """
        url += '?access_token={}'.format(self.TOKEN)
        logging.debug('requesting url: {}'.format(url))
        r = requests.get(url)
        return r.json()
