from datetime import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Account, Positions


class AccountTests(TestCase):
    def setUp(self):
        self.position = Positions.objects.create(
            position_name='admin'
        )

        self.user = Account.objects.create(
            first_name='test name',
            last_name='test last name',
            username='testuser',
            password='secret123',
            email='test@test.com',
            position=self.position,
            birth_date='2000-10-10',
            level=1,
            is_active=True,
        )

    def test_user(self):
        self.assertEqual(self.user.id, 1)
        self.assertEqual(self.user.position.position_name, 'admin')
        self.assertLess(self.user.birth_date, datetime.today().strftime('%Y-%m-%d'))
        self.assertTrue(self.user.is_active)

    def test_profile_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertContains(response, self.user.get_full_name())
        self.assertEqual(response.status_code, 200)
