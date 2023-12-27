from django.test import TestCase, LiveServerTestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Experience, Education
from selenium import webdriver
from selenium.webdriver.common.by import By


class AccountsModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="mohammad",
            password="Zaq11qaZ")

        self.client = Client()

    def test_create_education(self):
        edu = Education.objects.create(
            user=self.user.userprofile,
            university="ut",
            start_date="2020-10-10",
            end_date="2023-10-10",
            degree="master",
            field_of_study="cs",
            description="education test description")

        self.assertEqual(Education.objects.all().count(), 1)


class UserProfileModelTest(LiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            first_name='John',
            last_name='Doe')
        self.user_profile = self.user.userprofile
        self.user_profile.job_title = 'Developer'
        self.user_profile.bio = 'A test bio'
        self.user_profile.slug = "testuser"

        image_path = r"C:\Users\MohammadNPak\Desktop\profile.png"
        self.user_profile.picture = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(image_path, 'rb').read(),
            content_type='image/png')

        self.user_profile.save()

    def test_user_profile_str_representation(self):
        self.assertEqual(
            str(self.user_profile),
            f"UserProfile({self.user.first_name} {self.user.last_name})")

    def test_user_profile_get_absolute_url(self):
        self.assertEqual(
            self.user_profile.get_absolute_url(),
            f"/accounts/profile/{self.user_profile.slug}")

    def test_user_profile_page(self):
        driver = webdriver.Firefox()
        driver.get(
            f"{self.live_server_url}{self.user_profile.get_absolute_url()}")
        driver.implicitly_wait(10)

        user_full_name = driver.find_element(By.ID, "full_name").text
        self.assertEqual(
            user_full_name,
            self.user_profile.user.get_full_name())
