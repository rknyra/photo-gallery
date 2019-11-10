from django.test import TestCase
from .models import Location, Category, Image
import datetime as dt

#category test
class CategoryTestClass(TestCase):
    
    def setUp(self):
        self.Birthday = Category(category='Birthday')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Birthday,Category))
        
    def tearDown(self):
        Category.objects.all().delete()
        
#locaton test
class LocationTestClass(TestCase):
    def setUp(self):
        self.Diani = Location(location='Diani')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Diani,Location))
    
    def tearDown(self):
        Location.objects.all().delete()
        
 #image test
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name='Sunny birthday', description='Beach birthday', location='Diani', category='Birthday')
        self.assertTrue(isinstance(self.image,Image))
    
    def tearDown(self):
        Image.objects.all().delete()
         