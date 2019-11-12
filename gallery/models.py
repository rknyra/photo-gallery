from django.db import models
import datetime as dt
from pyuploadcare.dj.models import ImageField


#Category Model
class Category(models.Model):
    category = models.CharField(max_length =30)
    
    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()
    
    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

#Location Model
class Location(models.Model):
    location = models.CharField(max_length =70)
    
    def __str__(self):
        return self.location
    
    def save_locaton(self):
        self.save()
    
    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()
        

#Image Model
class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")
    name = models.CharField(max_length =70)
    description = models.CharField(max_length =120)
    post_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    # @classmethod
    # def today_photos(cls):
    #     today = dt.date.today()
    #     photos = cls.objects.filter(post_date__date = today)
    #     return photos
    
    # @classmethod
    # def days_photos(cls,date):
    #     photos = cls.objects.filter(pub_date__date = date)
    #     return photos
    
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__category=search_term)
        return photos
    
    @classmethod
    def filter_by_location(cls,search_term):
        photos = cls.objects.filter(location__location=search_term)
        return photos
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
    
    class Meta:
        ordering = ['post_date']
    
