from django.db import models

# Create your models here.

class Details(models.Model):
    seller_id=models.IntegerField()
    Flute_type=models.CharField(max_length=20)
    Price=models.IntegerField(default=0)
    Description=models.TextField()
    Youtube_link=models.CharField(max_length=50)
    video_id=models.CharField(default='',max_length=10)
    lenght=models.CharField(max_length=20)
    Materail=models.CharField(max_length=20)