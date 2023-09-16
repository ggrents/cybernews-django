from django.test import TestCase
from django.urls import reverse, resolve
from users.views import *

class TestUrls(TestCase) :
    def test_user_signup(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, SignUpView)


    def test_user_signin(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func.view_class, SignInView)

    def test_user_pass_change(self):
        url = reverse('change-password')
        self.assertEquals(resolve(url).func.view_class, PasswordChange)

