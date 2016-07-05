from django.shortcuts import render, get_object_or_404

from rest_condition import And, Or, Not
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.pagination import SmallTreePagination
from .serializers import FamilyMemberSerializer
from .models import FamilyMember
from .filters import ChildFilterBackend

class FamilyTreeViewSet(viewsets.ModelViewSet):
    serializer_class = FamilyMemberSerializer
    queryset = FamilyMember.objects.all()
    filter_backends = (
        filters.SearchFilter,
    )
    pagination_class = SmallTreePagination
    permission_class = (IsAuthenticated,)