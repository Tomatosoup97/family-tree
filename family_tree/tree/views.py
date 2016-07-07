from django.shortcuts import render, get_object_or_404
from django.utils import six 
from django.db.models import Q

from rest_condition import And, Or, Not
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin

from .pagination import SmallTreePagination
from .serializers import FamilyMemberSerializer
from .models import FamilyMember

class FamilyTreeViewSet(NestedViewSetMixin,
                        viewsets.ModelViewSet):
    serializer_class = FamilyMemberSerializer
    queryset = FamilyMember.objects.all()
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('first_name', 'last_name')
    ordering_fields = ('last_name', 'born')
    pagination_class = SmallTreePagination

class ParentViewSet(FamilyTreeViewSet):
    """
    List all member's parents
    """
    def get_queryset(self):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict:
            try:
                id = parents_query_dict['id']
                member = FamilyMember.objects.filter(id=id)
                parents_ids = member.values_list('parents__id')
                return FamilyMember.objects.filter(id__in=parents_ids)
            except ValueError:
                raise Http404
        else:
            return self.queryset

class SiblingViewSet(FamilyTreeViewSet):
    """
    List all member's siblings
    """
    def get_queryset(self):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict:
            try:
                id = parents_query_dict['id']
                member = FamilyMember.objects.filter(id=id)
                parents_ids = member.values_list('parents__id')
                # Exclude current member
                queryset = FamilyMember.objects.filter(
                            parents__in=parents_ids).exclude(id=id)
                return queryset
            except ValueError:
                raise Http404
        else:
            return self.queryset