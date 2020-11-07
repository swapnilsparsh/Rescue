from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

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
