
from rest_framework import serializers
from .models import Department,User, Ticket, TicketMessage


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'customer', 'department', 'priority', 'created_at']
        read_only_fields = ['customer']   

             
class TicketMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    def validate_ticket(self, value):
        user = self.context['request'].user
        if not user.is_staff and value.customer != user:
            raise serializers.ValidationError("You do not have permission to send a message for this ticket.")
        return value
    class Meta:
        model = TicketMessage
        fields = ['id', 'ticket', 'sender', 'message', 'created_at'] 
        read_only_fields = ['sender']
              