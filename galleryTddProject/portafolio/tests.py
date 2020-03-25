
from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from .models import Portafolio
import json

# Create your tests here.


class PortafolioTestCase(TestCase):

    def test_list_portafolios_status(self):
        url = '/portafolios/'
        response = self.client.get(url, Format='json')
        self.assertEqual(response.status_code, 200)
