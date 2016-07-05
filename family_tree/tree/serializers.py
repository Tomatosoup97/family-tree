from rest_framework import serializers

from .models import FamilyMember

class FamilyMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = FamilyMember
        fields = (
            'id', 'last_login', 'username', 'password', 'first_name',
            'last_name', 'email', 'date_joined', 'is_staff', 'is_active',
            'groups', 'user_permissions', 'born', 'died')
        
        readonly_fields = (
            'last_login','date_joined', 'is_staff',
            'is_active', 'user_permissions', 'groups',)

    def validate(self, data):
        if data['father__born'] > data['born'] or \
                data['mother__bron'] > data['born']:
            raise serializer.ValidationError(
                'You can not be older than your parent!')
