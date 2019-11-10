from django.db import models
import datetime as dt


#Category Model
class Category(models.Model):
    category = models.CharField(max_length =30)
    
    def __str__(self):
        return self.category

#Location Model
class Location(models.Model):
    location = models.CharField(max_length =70)
    
    def __str__(self):
        return self.location

#Image Model
class Image(models.Model):
    image = models.ImageField(upload_to='images/', default='image.png')
    name = models.CharField(max_length =70)
    description = models.CharField(max_length =120)
    post_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    @classmethod
    def today_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(post_date__date = today)
        return photos
    
    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos
    
    def save_image(self):
        self.save()
    
    class Meta:
        ordering = ['post_date']
    
