from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK

# Create your tests here.


class PizzaTest(APITestCase):

    def test_pizza_list(self):

        response = self.client.get('shop/pizza/')
        self.assertHTMLEqual(HTTP_200_OK, response.status_code)
