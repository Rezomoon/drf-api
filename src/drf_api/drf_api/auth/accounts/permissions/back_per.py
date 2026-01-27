from rest_framework import permissions

#

class FirstPermissions(permissions.BasePermission) : 
    message = "User Nemeshnasam !"
    def has_permission(self, request, view):
        ip_addr     = request.META["REMOTE_ADDR"]
        # blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists() 
        # return not blocked
        return super().has_permission(request, view)
    pass

class IsAdminPermissions(permissions.BasePermission) : 
    def has_permission(self, request, view):

        return bool(request.user.is_admin and request.user.is_staff and request.user.is_verified and request.user.is_active)
    