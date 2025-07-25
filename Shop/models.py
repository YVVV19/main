from django.db import models
from django.db.models import Model, CharField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='Shop/images/user_avatar', null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Shop/images/admin_add', blank=True, null=True)
    new = models.BooleanField(default=False)


class Review(models.Model):
    review = models.CharField(max_length=250)
    name = models.CharField(max_length=250)


class Stuff(models.Model):
    stuff_id = models.IntegerField()
    stuff_name = models.CharField(max_length=30)
    stuff_desc = models.CharField(max_length=257)
    photo = models.CharField(max_length=100)
    price = models.FloatField()
    
    def publish(self):
        self.save()

class Person(models.Model):
    person_id = models.IntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=257)
    phone = models.CharField(max_length=12)
    admin = models.BooleanField()

    def publish(self):
        self.save()


class Admin_Table(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=75)
    phone = models.IntegerField()
