from django.db import models

# Create your models here.

class User(models.Model):
    company = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.company
