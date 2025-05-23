from django.db import models
from Accounts.models import Account
import django_jalali.db.models as jalali_models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    created_at = jalali_models.jDateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/Category', blank=False, null=False)

    def __str__(self):
        return self.name


def get_default_category():
    default_cat = Category.objects.first()
    return default_cat.id if default_cat else None


class Article(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=get_default_category, null=False,
                                 blank=False)
    title = models.CharField(max_length=70, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    preview_description = models.TextField(blank=False, null=False, max_length=300)
    image = models.ImageField(upload_to='images/Article', blank=False, null=False)
    created_at = jalali_models.jDateField(auto_now_add=True)
    updated_at = jalali_models.jDateField(auto_now=True)
    keywords = models.TextField(blank=True, null=True, max_length=300)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
