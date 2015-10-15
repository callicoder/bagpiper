from django.db import models

# Create your models here.

class Coupon(models.Model):
	code = models.CharField(max_length=255, unique=True, null=False)
	description = models.TextField(default=None)
	discount_value = models.DecimalField(decimal_places=2, max_digits=10, default=0)
	valid_from = models.DateField()
	valid_till = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.code	
