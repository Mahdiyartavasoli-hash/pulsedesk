from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        customer = getattr(obj, 'customer', None) 
        ticket = getattr(obj, 'ticket', None)

        if  customer:
           return customer == request.user
        elif ticket:
            return ticket.customer == request.user
        return False 