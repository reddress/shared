from django.shortcuts import render
from django.http import HttpResponse
from pyrobot import Robot

# Create your views here.
def index(request):

    # robot = Robot()
    
    print("to console")
    return HttpResponse("the index")
    
