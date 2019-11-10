from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.home,name='home'),
    url('^today/$',views.photos_of_day,name='photosToday')
]
