from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
import string, random

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		"""
			Creates and saves a user with the given email, username and password
		"""
		if not email:
			raise ValueError('Users must have a valid emails address.')
		
		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username')

		user = self.model(
			email = self.normalize_email(email), username = kwargs.get('username')
		)

		user.set_password(password)
		user.ref_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
		user.save()

		return user

	def create_superuser(self, email, password, **kwargs):
		"""
			Creates and saves a superuser with the given email, username and password
		"""
		user = self.create_user(email, password, **kwargs)

		user.is_admin = True
		user.save()

		return user

class User(AbstractBaseUser):
	email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
	username = models.CharField(max_length=40, unique=True)

	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)

	ref_code = models.CharField(max_length=255, blank=True)
	ref_bonus = models.IntegerField(default=0)
	
	is_admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __unicode__(self):
		return self.email