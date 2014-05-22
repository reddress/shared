from django.shortcuts import render

from mult.models import MyItem

# Create your views here.
def index(request):
    items = MyItem.objects.all()

    return render(request, 'mult/index.html',
                  {'items': items})
