from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_extensions import routers

from . import views

router = routers.ExtendedDefaultRouter()
family_routes = router.register(
        r'family',
        views.FamilyTreeViewSet,
        base_name='member')
        
family_routes.register(r'children',
                views.FamilyTreeViewSet,
                base_name='member-child',
                parents_query_lookups=['parents'])

family_routes.register(r'parents',
                views.ParentViewSet,
                base_name='member-parent',
                parents_query_lookups=['id'])

urlpatterns = [
    url(r'^', include(router.urls)),
]