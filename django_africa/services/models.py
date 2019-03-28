from django.db import models

# Create your models here.

# service appointment form
class Signup_Form(models.Model):
    # time = models.DateTimeField('appointment submitted')
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 50)
    number = models.CharField(max_length = 12)

    def __str__(self):
        return self.name