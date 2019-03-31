from django.db import models

# Create your models here.

# service appointment form
class Service_Appt(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 50)
    number = models.CharField(max_length = 12)

    def __str__(self):
        return self.name