from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status, views, viewsets
from users.models import User
from users.permissions import IsAccountOwner
from users.serializers import UserSerializer
from rest_framework.response import Response
import json

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			User.objects.create_user(**serializer.validated_data)
			return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

		return Response({
			'status': 'Bad Request',
			'message': 'User could not be created with received data.'
		}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
	def post(self, request, format=None):
		data = json.loads(request.body)
		email = data.get('email', None)
		password = data.get('password', None)

		user = authenticate(email=email, password=password)
		
		if user is not None:
			if user.is_active:
				login(request, user)
				serialized = UserSerializer(user)
				return Response(serialized.data)
			else:
				return Response({
					'status': 'Unauthorized',
					'message': 'This account has been disabled.'
				}, status=status.HTTP_401_UNAUTHORIZED)
		else:
			return Response({
				'status': 'Unauthorized',
				'message': 'Username/Password combination invalid.'
			}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
	permission_classes = (permissions.IsAuthenticated,)
	
	def post(self, request, format=None):
		logout(request);
		return Response({}, status=status.HTTP_204_NO_CONTENT)	
