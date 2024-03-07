from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class IncomeTests(TestCase):
    fixtures = ['user.json', 'courier.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.fixture = [
            {'courier': 1, 'amount': 1000},
            {'courier': 1, 'amount': 3000},
            {'courier': 1, 'amount': -500}
        ]

    def test_integration_income_item_green(self):
        data = {
            "courier": 1,
            "amount": 2000
        }

        for item in self.fixture:
            self.client.post(reverse("income-item"), data=item)

        response = self.client.post(reverse("income-item"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(5500, response.data['amount'])
