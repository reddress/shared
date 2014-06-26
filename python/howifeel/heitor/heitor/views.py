from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout

def do_logout(request):
    logout(request)
    return redirect("/")

def index(request):
    return HttpResponse('<a href="/howifeel/">How I feel</a>')
