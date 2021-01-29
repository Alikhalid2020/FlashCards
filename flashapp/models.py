from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_photo = models.ImageField(upload_to="images/")
    email = models.EmailField(max_length=200)
    member_since = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Deck(models.Model):
    title = models.TextField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Card(models.Model):
    title = models.TextField(max_length=150)
    notes = models.TextField(max_length=300)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)