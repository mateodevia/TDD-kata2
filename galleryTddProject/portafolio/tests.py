
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

    def test_count_portafolios_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Portafolio.objects.create(user=user_model)
        Portafolio.objects.create(user=user_model)

        response=self.client.get('/portafolios/')
        current_data=json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data),2)


    def test_add_user(self):
        response=self.client.post('/portafolio/addUser/',json.dumps({"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5", "email": "test@test.com"}), content_type='application/json')
        current_data=json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'],'testUser')
