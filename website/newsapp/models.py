from django.db import models
from django.utils import timezone

# Create your models here.


    


class News(models.Model):
    
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())
    image = models.ImageField(upload_to='pics')
 


    def __str__(self):
        return self.author


class home_news(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.title


class Sportsnews(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.author


class Registrationdata(models.Model):

    
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username
class loginn(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
