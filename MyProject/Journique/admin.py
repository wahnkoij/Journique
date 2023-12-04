from django.contrib import admin
from .models import UserProfile, Image, Pin

admin.site.register(UserProfile)
admin.site.register(Image)
admin.site.register(Pin)
