# Lee Kusowski
# Webhooks
# Dec 05 2025 

# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse

# from .models import CustomUser

# class AccountTest(TestCase):
#     '''Account Tests'''

#     @classmethod
#     def setUpTestData(cls):
#         """Set Up Test Data - Create Test User"""
#         cls.user = get_user_model().objects.create_user(
#             username="testuser",
#             email="test@email.com",
#             password="secret",
#         )

#     """Sign Up Page Tests"""

#     def test_url_exists_at_correct_location(self):
#         """Test URL is at Correct Location"""

#         response = self.client.get("/accounts/signup/")
#         self.assertEqual(response.status_code, 200)

#     def test_signup_view_name(self):
#         """Test Sign Up View Name Correct"""

#         response = self.client.get(reverse("signup"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "registration/signup.html")

#     def test_signup_form(self):
#         """Test Sign Up Form"""

#         response = self.client.post(
#             reverse("signup"),
#             {
#                 "username": "testuser",
#                 "email": "test@email.com",
#                 "password1": "testpass123",
#                 "password2": "testpass123",
#             },
#         )
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(get_user_model().objects.all().count(), 1)
#         first_user = get_user_model().objects.first()

#         self.assertEqual(first_user.username, "testuser")
#         self.assertEqual(first_user.email, "test@email.com")

#     """ Account Model Tests """    

#     def test_customuser_model(self):
#         """Test CustomUser model working as intended"""
#         self.assertEqual(self.user.get_absolute_url(), "/accounts/1/")

#     def test_url_exists_at_correct_location_detailview(self):
#         """Test URL exists at Correct Location for CustomUser Detail View"""
                
#         self.client.force_login(self.user)

#         response = self.client.get("/accounts/1/")
#         self.assertEqual(response.status_code, 200)

#     '''Account View Tests'''

#     def test_customuser_detailview(self):
#         """Test CustomUser Detail View"""
                
#         self.client.force_login(self.user)

#         response = self.client.get(
#             reverse("account_detail", kwargs={"id": self.user.id}),
#         )
#         no_response = self.client.get("/accounts/1000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertTemplateUsed(response, "account_detail.html")

#     def test_customuser_updateview(self):
#         """Test CustomUser Update View"""

#         self.client.force_login(self.user)

#         response = self.client.get(reverse("account_edit", args="1"))

#         data = {
#             "username": "testuser",
#             "first_name": "test",
#             "last_name": "user",
#             "email": "test@email.com",
#         }

#         response = self.client.post(
#             reverse("account_edit", args="1"),
#             data,
#         )
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(CustomUser.objects.last().username, "testuser")
#         self.assertEqual(CustomUser.objects.last().email, "test@email.com")

from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False)
