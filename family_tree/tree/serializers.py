from rest_framework import serializers

from .models import FamilyMember

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = (
            'id', 'first_name', 'last_name', 'family_name', 'gender',
            'image', 'born', 'died', 'parents',)

    def validate(self, data):
        for parent in data['parents']:
            if parent.born > data['born']:
                raise serializer.ValidationError(
                    'You cannot be older than you parent {parent}!'.format(
                                                            parent=parent))
        return data