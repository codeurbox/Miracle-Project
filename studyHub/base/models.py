from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(null=True, default="avatar.svg")

class GroupInterest(models.Model):
    interest = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ManyToManyField(User)
    group = models.ManyToManyField('Group')

class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    joiners = models.ManyToManyField(User, related_name="joiners", blank=True)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    logo = models.ImageField(null=True, default="logo.svg")

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)





