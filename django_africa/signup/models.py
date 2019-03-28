from django.db import models

# Create your models here.

#sign up form
class Signup_Form(models.Model):
    # time = models.DateTimeField('appointment submitted')
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 50)
    number = models.CharField(max_length = 12)
    role = models.CharField(max_length = 200, null = True)
    dob = models.CharField(max_length = 200, default='00/00/0000')
    last_employment = models.CharField(max_length = 200, default='none')
    criminal = models.BooleanField()
    resume = models.FileField(upload_to='resumes/', null=True)

    def __str__(self):
        return self.name