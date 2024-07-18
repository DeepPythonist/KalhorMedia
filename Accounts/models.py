from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Rank(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


def get_default_rank():
    default_rank = Rank.objects.first()
    return default_rank.id if default_rank else None


class Account(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    full_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    rank = models.ForeignKey(Rank, on_delete=models.SET_DEFAULT, default=get_default_rank, blank=False,
                             null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/profile_pictures')

    def __str__(self):
        return self.full_name
