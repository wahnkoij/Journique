from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Using the default image
    image = models.ImageField(upload_to='default_profile_image/', default='default_profile_image/blank_profile.png')
    preferred_categories = models.ManyToManyField(Category, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a user profile when a new user is created.
    """
    if created and not hasattr(instance, 'userprofile'):
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler to save the user profile when the associated user is saved.
    """
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()


class Pin(models.Model):
    """
    Model representing a Pin, associated with a user and a category.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='pins/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, default=timezone.now)

    def delete_pin(self):
        """
        Method to mark a pin as deleted.
        """
        self.is_deleted = True
        self.save()
