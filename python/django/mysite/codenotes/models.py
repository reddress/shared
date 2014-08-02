from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import utc, localtime

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=220)
    date = models.DateTimeField(default=timezone.now)
    url = models.URLField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Sample(models.Model):
    post = models.ForeignKey(Post)
    language = models.ForeignKey(Language)
    code = models.TextField()
    def __str__(self):
        return str(self.language) + ": " + self.code[:80]
