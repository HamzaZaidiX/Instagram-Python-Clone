from django.test import TestCase
from .models import Comments,Profile,Image
# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.animal= Image()

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.animal,Image))  

    def test_save_method(self):
        self.animal.save_image()
        images = Image.objects.all() 
        self.assertTrue(len(images)>0)      
    

    def test_update_method(self):
        self.animal.update_image()
        images = Image.objects.filter(id=2).update(image='zebra') 
        self.assertTrue(len(images)==0)   

    def test_delete_method(self):
        self.animal.delete_image()
        images=Image.objects.filter(animal=zebra).delete() 
        self.assertTrue(len(images)==0)     