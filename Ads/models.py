from django.db import models


# Create your models here.


class Ads(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/Ads')

    def __str__(self):
        return self.name

