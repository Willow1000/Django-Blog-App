from django.test import TestCase
from .models import CustomUser
# Create your tests here.

class TestCustomUser(TestCase):
     def test_model(self):
          
          customuser = CustomUser(
               role="blogger",
               username = "user",
               first_name = "user",
               last_name = "some",
               email = "user@mail.com",
               password = 'qwerty@123'
          )
          self.assertEqual(customuser.role,'blogger')
          self.assertEqual(customuser.username,'user1')