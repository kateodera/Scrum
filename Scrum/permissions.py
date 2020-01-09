from rest_framework import permissions

#
class SrumMasterPermissions(permissions.BasePermission):
    message = "You Are Not a Scrum Master"

    def has_permission(self, request, view):

        print(request.user.is_ScrumMaster)
        # if request.user.is_ScrumMaster:
        #     return True
        # return True
        return request.user.is_ScrumMaster


class DeveloperPermissions(permissions.BasePermission):
    message = "You Are Not a Developer"

    def has_permission(self, request, view):
        return request.user.is_Developer



