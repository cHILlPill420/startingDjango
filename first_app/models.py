from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True)
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topics = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete = models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

#User Models/ Registration
class UserProfileInfo(models.Model):
    #User provides all fields like username,firstname, lastname, etc
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #one to one field lets you add other fields for the User
    #additional fields
    portfolio_site = models.URLField(blank = True, unique = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username