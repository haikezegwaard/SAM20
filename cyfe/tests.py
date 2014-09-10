from django.test import TestCase
import views
from django.http import HttpRequest, HttpResponse
# Create your tests here.

class CyfeNikiTests(TestCase):

    def test_salecount_returns_httpresponse(self):
        request = HttpRequest()
        request.GET = { 'project': '/projects/54/AMVP9518'}

        result = views.nikisalecount(request)
        assert isinstance(result, HttpResponse)