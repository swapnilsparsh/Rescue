from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class contact(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contact", null=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    Father = "Father"
    Mother = "Mother"
    Brother = "Brother"
    Sister = "Sister"
    Husband = "Husband"
    Friend = "Friend"
    Relative = "Relative"
    Other = "Other"
    relations = (
        (Father, "Father"),
        (Mother, "Mother"),
        (Brother, "Brother"),
        (Sister, "Sister"),
        (Husband, "Husband"),
        (Friend, "Friend"),
        (Relative, "Relative"),
        (Other, "Other"),
    )
    relation = models.CharField(max_length=10, choices=relations, default=Other)

    def __str__(self):
        return self.name


class Login(models.Model):

    Username_or_Email = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
