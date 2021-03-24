from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

# Create your models here.
class contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="contact", null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    Father = 'Father'
    Mother = 'Mother'
    Brother = 'Brother'
    Sister = 'Sister'
    Husband = 'Husband'
    Friend = 'Friend'
    Relative = 'Relative'
    Other = 'Other'
    relations = (
        (Father, 'Father'),
        (Mother, 'Mother'),
        (Brother, 'Brother'),
        (Sister, 'Sister'),
        (Husband, 'Husband'),
        (Friend, 'Friend'),
        (Relative, 'Relative'),
        (Other, 'Other'),
    )
    relation = models.CharField(max_length=10, choices=relations, default=Other)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')    
    about_me = models.TextField(blank=True, max_length = 500, default= "")
    phone_number = models.IntegerField(blank=True, null = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)