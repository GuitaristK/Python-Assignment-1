from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def myView(request):
    return HttpResponse(("Hello World!!"))
def index(request):
    return HttpResponse(("Hello and have a nice day""Today's date is ",datetime.now() ))
