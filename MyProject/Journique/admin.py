from django.contrib import admin
from .models import UserProfile, Pin, Category

admin.site.register(UserProfile)
admin.site.register(Pin)
admin.site.register(Category)
