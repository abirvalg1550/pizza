from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from .models import Pizza

# Create your tests here.


class PizzaTest(APITestCase):

    # Подготовка перед тестом
    #  мы тут заранее подготовили несколько объектов класса пицц,
    #  для того, чтобы тест проходил.
    def setUp(self) -> None:

        Pizza.objects.create(pk=1)
        Pizza.objects.create(pk=2)

    def test_pizza_list(self):

        response = self.client.get('/shop/pizza/')
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual([{'id': 1}, {'id': 2}], response.json())

    def test_pizza_details(self):

        response = self.client.get('/shop/pizza/1/')
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual({'id': 1}, response.json())

    def test_pizza_not_found(self):
        response = self.client.get('/shop/pizza/3/')
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)
