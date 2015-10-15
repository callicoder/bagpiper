from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
	def has_object_permission(self, request, view, account):
		if request.user:
			return request.user.is_admin
		return False

