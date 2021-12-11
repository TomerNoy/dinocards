from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileType(models.Model):
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileType = models.ForeignKey(ProfileType, on_delete=models.CASCADE)
    coins = models.PositiveIntegerField(default=200)

    def __str__(self):
        return f'{self.user.username}'


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
