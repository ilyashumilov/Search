from django.db import models

# Create your models here.

class client(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)

    def __str__(self):
        return str(self.firstname) + ' ' + str(self.lastname)