from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.conf import settings # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore

# /////////////////////////////////////////////////////////////////////

class Book(models.Model):
    language = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title
    
# /////////////////////////////////////////////////////////////////////

class borrowedb(models.Model):
    borrower_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    national_id = models.CharField(max_length=20)
    isbn = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    email = models.EmailField()
    def remaining_days(self):
        from django.utils import timezone # type: ignore
        remaining = self.due_date - timezone.now().date()
        return remaining.days
    
# /////////////////////////////////////////////////////////////////////

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

# /////////////////////////////////////////////////////////////////////
