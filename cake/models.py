from django.db import models

# Create your models here.
class DataDescr(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    