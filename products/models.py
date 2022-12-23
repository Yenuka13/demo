from django.db import models


class Product(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Url = models.CharField(max_length=2083)
    Image_URL = models.CharField(max_length=2083)
    Button_label = models.CharField(max_length=255)
