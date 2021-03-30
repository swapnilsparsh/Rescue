from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Pointer to the Filesystem where we store our static files
fs = FileSystemStorage(location=settings.STATICFILES_DIRS[0])

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


class Login(models.Model):
    
    Username_or_Email= models.CharField(max_length=100)
    password = models.CharField(max_length=32)

# Model to create the items for slideshow

class SlideShowItem(models.Model):
    name = models.CharField(verbose_name="Name",max_length=30)
    image = models.ImageField(upload_to="Images/slideshow",storage=fs)
    content = models.CharField(verbose_name="Enter content only upto 200 characters",max_length=200)
    read_more = models.CharField(verbose_name="Add a read more link to related article",max_length=1000)

    def __str__(self):
        return self.name
    


    

