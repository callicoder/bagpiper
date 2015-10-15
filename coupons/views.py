from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from coupons.models import Coupon
from coupons.permissions import IsAdminUser
from coupons.serializers import CouponSerializer

# Create your views here.

class CouponViewSet(viewsets.ModelViewSet):
	queryset = Coupon.objects.order_by('-created_at')
	serializer_class = CouponSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)
		return (permissions.IsAuthenticated(), IsAdminUser(),)
		
	def perform_create(self, serializer):
		instance = serializer.save()
		return super(CouponViewSet, self).perform_create(serializer)
