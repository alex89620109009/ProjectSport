from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=20, null=False)
    thirdName = models.CharField(max_length=20)
    contrie = models.CharField(max_length=30, null=False)
    region = models.CharField(max_length=40, null=False)
    city = models.CharField(max_length=40, null=False)
    bio = models.BooleanField(default=True, null=False)
    photo = models.ImageField()
    DateOfBirth = models.DateField(null=False)
    club = models.CharField(max_length=40)
    