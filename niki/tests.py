from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class IndexTest(TestCase):
    def test_sanity(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)