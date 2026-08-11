from rest_framework import viewsets
from .models import Department, Ticket, TicketMessage
from .serializers import DepartmentSerializer, TicketSerializer, TicketMessageSerializer
from .permissions import IsOwnerOrStaff


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrStaff]
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Ticket.objects.all()
        else:
            return Ticket.objects.filter(customer=user)
    


class TicketMessageViewSet(viewsets.ModelViewSet):
    queryset = TicketMessage.objects.all()
    serializer_class = TicketMessageSerializer



