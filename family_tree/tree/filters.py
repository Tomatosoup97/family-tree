from rest_framework import filters

class ChildFilterBackend(filters.BaseFilterBackend):
    """
    Return only children of current user
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(children=request.user.child)

class ParentFilterBackend(filters.BaseFilterBackend):
    """
    Return only parents of current user
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(parents=request.user.child)