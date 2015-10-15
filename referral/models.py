from django.db import models
from users.models import User
# Create your models here.

class Referral(models.Model):
	referrer = models.ForeignKey(User, related_name='referrer_user')
	referee = models.ForeignKey(User, related_name='referrer')
	status = models.BooleanField(default=False)

