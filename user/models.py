from django.db import models

class data(models.Model):
    image = models.ImageField(upload_to='images/')
    text =  models.CharField(max_length=50)
