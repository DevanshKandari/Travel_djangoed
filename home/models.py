from django.db import models

# Create your models here.

class inq(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    msg = models.TextField()
     
    def __str__(self) :
        return self.name

class blog(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    pic = models.ImageField(upload_to="new")