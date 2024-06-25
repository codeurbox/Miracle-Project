from django.contrib import admin
from .models import UserProfile, Group, GroupInterest

admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(GroupInterest)
