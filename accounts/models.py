from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
        @receiver(post_save, sender=User)
        def create_or_update_user_profile(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(user=instance)
            instance.profile.save()
    
class Department(models.Model):
    name = models.CharField(max_length=128)
    employees = models.ManyToManyField(User, default=None, blank=True, related_name='employees')

    def __str__(self):
        return self.name
    
    