from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image, Location, Category

#views
def home(request):
    date = dt.date.today()
    photos = Image.objects.all()

    return render(request, 'all-photos/home.html', {'date':date, 'photos':photos})


def photos_of_day(request):
    date = dt.date.today()
    
    #function to convert date object to find the exact day
    day = convert_dates(date)
  
    return render(request, 'all-photos/home.html', {'date':date,})


def convert_dates(dates):
    #function that gets the weekday number for a given date
    day_number = dt.date.weekday(dates)
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    #return the actual day of the week
    day = days[day_number]
    
    return day

#view function to present photos from past-days
def past_days_photos(request,past_date):
    
    try:
        #convert data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        #raise error 404 when ValueError is thrown
        raise Http404()
        assert False
    
    day = convert_dates(date)
    if date == dt.date.today():
       return redirect(photos_of_day)
    return render(request, 'all-photos/past-photos.html', {'date':date})