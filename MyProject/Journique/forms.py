from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *


class UserProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'image', 'preferred_categories']
        widgets = {'preferred_categories': forms.CheckboxSelectMultiple(choices=Category.objects.all())}


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['description', 'file', 'category']


class PreferredCategoriesForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['preferred_categories']
        widgets = {'preferred_categories': forms.CheckboxSelectMultiple(choices=Category.objects.all())}
