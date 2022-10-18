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

# class Profile(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to='profile')
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username
    
#     @property
#     def imageURL(self):
#         try:
#             url = self.avatar.url
#         except:
#             url = ''
#         return url
    
#     def save(self):
#         super().save()
        
#         img = Image.open(self.avatar.path)
        
#         if img.height > 100 or img.width > 100 :
#             new_img = (100 , 100)
            
#             img.thumbnail(new_img)
            
#             img.save(self.avatar.path)