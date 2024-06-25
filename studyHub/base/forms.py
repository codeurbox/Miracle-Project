from django.forms import ModelForm
from .models import Group
from django import forms

class createGroupForm (forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "description", "logo"]