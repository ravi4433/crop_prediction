from django.db import models

class EnquiryData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    query = models.CharField(max_length=250)

