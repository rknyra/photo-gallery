from django.shortcuts import render
from django.http import HttpResponse

#views
def home(request):
    return HttpResponse('Welcome to my photogallery')
