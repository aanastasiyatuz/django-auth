import requests
from django.test import TestCase

class CheckAuthTest(TestCase):
    def test_login(self):
        su_response = requests.post("http://127.0.0.1:8000/account/login/", {"email":"admin@admin.com", "password":"1"})
        u_response = requests.post("http://127.0.0.1:8000/account/login/", {"email":"test@gmail.com", "password":"string"})

        self.assertEqual(su_response.status_code, 200)
        self.assertEqual(u_response.status_code, 200)

        self.assertIn("access", su_response.json())
        self.assertIn("refresh", su_response.json())

        self.assertIn("access", u_response.json())
        self.assertIn("refresh", u_response.json())
