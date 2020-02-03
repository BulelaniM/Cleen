from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField
from star_ratings.models import Rating

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=50)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	cellphone = models.CharField(max_length=10)
	address1 = AddressField()
	address2 = AddressField(related_name='+', blank=True, null=True)
	ratings = Rating()

	def __str__(self):
		return f'{self.user.username} Profile'
		return f'{self.user.name} Profile'
		return f'{self.user.surname} Profile'

# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     otp1 = models.IntegerField(null=True)
#     phoneno1 = models.CharField(max_length=10)