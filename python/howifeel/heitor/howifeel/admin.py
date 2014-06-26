from django.contrib import admin
from .models import Diary, Entry, Feeling

# Register your models here.
admin.site.register(Diary)
admin.site.register(Entry)
admin.site.register(Feeling)
