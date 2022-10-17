from email.mime import image
from django.db import models
from django.contrib.auth.models import User ,AbstractUser
from PIL import Image

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg' , upload_to='profile_')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    def save(self):
        super().save()
        
        img = Image.open(self.avatar.path)
        
        if img.height > 100 or img.width > 100 :
            new_img = (100 , 100)
            
            img.thumbnail(new_img)
            
            img.save(self.avatar.path)