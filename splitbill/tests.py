from django.test import TestCase
from django.test import Client

# Create your tests here.
class TestUpload(TestCase):
    def test_csv(self):
        c = Client()
        response = c.post('/upload')


