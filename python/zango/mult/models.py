from django.db import models

class MyItem(models.Model):
    myval = models.DecimalField(max_digits=18, decimal_places=6)
    def __str__(self):
        return str(self.myval)

