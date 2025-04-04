# jelapp/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Kezikonyv, Gyakorlo, Fogalom

class ModelTests(TestCase):
    def test_kezikonyv_creation(self):
        kezikonyv = Kezikonyv.objects.create(
            cim="Teszt kézikönyv",
            leiras="Ez egy teszt leírás",
            kategoria="Teszt"
        )
        self.assertEqual(kezikonyv.cim, "Teszt kézikönyv")
        self.assertEqual(str(kezikonyv), "Teszt kézikönyv")

class ViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "JelSmart")

    def test_kezikonyvek_view(self):
        Kezikonyv.objects.create(
            cim="Teszt kézikönyv",
            leiras="Teszt leírás",
            kategoria="Teszt"
        )
        response = self.client.get(reverse('kezikonyvek'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teszt kézikönyv")