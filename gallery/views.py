from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

#views
def home(request):
    return HttpResponse('Welcome to my photogallery')


def photos_of_day(request):
    date = dt.date.today()
    
    #function to convert date object to find the exact day
    day = convert_dates(date)
    html = f'''
    <html>
        <body>
            <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)

def convert_dates(dates):
    #function that gets the weekday number for a given date
    day_number = dt.date.weekday(dates)
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    #return the actual day of the week
    day = days[day_number]
    
    return day

def past_days_photos(request,past_date):
    #convert data from the string url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    day = convert_dates(date)
    html = f'''
        <html>
            <body> 
                <h1> Photos for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)