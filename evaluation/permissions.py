

from rest_framework.permissions import BasePermission

class isStudentUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "student":
            return True
        else:
            return False