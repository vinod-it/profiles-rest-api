from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit there own profile"""

    def has_object_permission(self,request,view, obj):
        """check user trying to edit their own profies"""
        if(request.method in permissions.SAFE_METHODS):
            return True

        return obj.id == request.user.id
