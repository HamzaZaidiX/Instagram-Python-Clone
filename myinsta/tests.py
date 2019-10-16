from django.test import TestCase
from .models import Comments,Profile,Image
# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image= Image()

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))     
