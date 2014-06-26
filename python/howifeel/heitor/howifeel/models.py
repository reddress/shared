import datetime

from django.db import models

from django.contrib.auth.models import User

# An user may have more than one diary.
# A diary is made of entries, each has a date, content, list of "feelings",
# and a subjective percentage "energy rating"

class Diary(models.Model):
    class Meta:
        verbose_name_plural = "Diaries"
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Feeling(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    # entries = models.ManyToManyField(Entry, null=True, blank=True)
    def __str__(self):
        return self.name

class Entry(models.Model):
    class Meta:
        verbose_name_plural = "Entries"
    user = models.ForeignKey(User)
    diary = models.ForeignKey(Diary)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    feelings = models.ManyToManyField(Feeling, null=True, blank=True)
    energy = models.IntegerField(null=True, blank=True)
    mood = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.title if self.title else "Untitled"
