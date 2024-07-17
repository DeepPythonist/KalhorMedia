from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('author/<str:name>', views.author, name='author'),
    path('category/<str:name>', views.category_detail, name='category'),
    path('article/<str:name>', views.article_detail, name='article'),
]
