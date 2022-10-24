from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True ,blank=True , upload_to='profile')
    bio = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.username
    
    @property
    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
