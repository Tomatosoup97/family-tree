from rest_framework import serializers

from .models import FamilyMember

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = (
            'first_name', 'last_name', 'family_name', 'image',
            'born', 'died', 'parents', 'children')

    def validate(self, data):
        for parent in data['parents']:
            if parent.born > data['born']:
                raise serializer.ValidationError(
                    'You cannot be older than you parent {parent}!'.format(
                                                            parent=parent))
        for child in data['children']:
            if child.born < data['born']:
                raise serializer.ValidationError(
                    'You cannot be younger than you child {child}!'.format(
                                                            child=child))
        return data