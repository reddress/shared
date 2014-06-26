from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required

# from .models import is_parent

@login_required
def index(request):
    return render(request, 'howifeel/index.html')

@login_required
def view_diary(request):
    return HttpResponse("View last few entries")

@login_required
def view_entry(request):
    return HttpResponse("View entry")

@login_required
def search(request):
    return HttpResponse("List of matching entries")
