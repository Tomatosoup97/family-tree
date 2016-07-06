from rest_framework import filters

class ChildFilterBackend(filters.BaseFilterBackend):
    """
    Return only children from current user
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(children__parent=request.user.id)

class ParentFilterBackend(filters.BaseFilterBackend):
    """
    Return only parents from current user
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(parents__children=request.user.id)