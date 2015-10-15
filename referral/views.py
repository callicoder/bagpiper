from django.shortcuts import render
from django.db import transaction
from rest_framework.decorators import api_view
from users.models import User
from referral.models import Referral
from rest_framework.response import Response
from referral.constants import *
# Create your views here.

@api_view()
@transaction.atomic
def verify_referral(request, pk):

	try: 
		referrer_user = User.objects.get(ref_code=pk)
	except:
		return Response({'success': False, 'message': 'Invalid referral code'})

	referee_user = request.user

	if referrer_user.username == referee_user.username:
		return Response({'success': False, 'message': 'Invalid referral code'})

	if Referral.objects.filter(referee=referee_user).exists():
		return Response({'success': False, 'message': 'You have already used a referral code'})		

	referrer_user.ref_bonus += 	referrer_bonus
	referee_user.ref_bonus += referee_bonus

	referrer_user.save()
	referee_user.save()

	Referral.objects.create(
		referrer = referrer_user, referee = referee_user, status = True
	)

	return Response({'success': True, 'message': 'Referral bonus added to your account'})

