from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home,name='home'),
    url('^gallery/$',views.home,name='gallery'),
    url('^today/$',views.photos_of_day,name='photosToday'),
    url('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name='pastPhotos')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)