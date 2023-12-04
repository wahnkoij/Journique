from django import forms
from .models import Pin


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['title', 'description', 'image', 'user', 'created_at']
