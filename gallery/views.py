from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image, Location, Category

#views
def home(request):
    # date = dt.date.today()
    photos = Image.objects.all()

    return render(request, 'all-photos/home.html', {'photos':photos})


def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
    
def search_by_location(request, search_term):
    location = Image.filter_by_location(search_term)
    message = f"{search_term}"
    
    return render (request,'all-photos/location.html',{"message":message,'photos': location})