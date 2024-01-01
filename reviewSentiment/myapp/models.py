from django.db import models

# Create your models here.

class BusinessItem(models.Model):
    name= models.CharField(max_length=200)
    yelp_url=models.CharField(max_length=1000)
    yelp_avg_sentiment = models.FloatField(null=True, blank=True)