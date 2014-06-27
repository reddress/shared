from django.shortcuts import redirect
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def do_logout(request):
    logout(request)
    return redirect("/")

@login_required
def home(request):
    return HttpResponse('<a href="/accounts/logout/"> log out</a>')
