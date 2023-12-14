from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *


class UserProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'bio']


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['description', 'file', 'user', 'category']