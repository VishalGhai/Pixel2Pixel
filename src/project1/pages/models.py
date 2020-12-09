from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="static/project1",default="default.png")
    w=models.IntegerField(default=300)
    h=models.IntegerField(default=300)