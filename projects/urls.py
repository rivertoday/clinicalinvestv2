__author__ = 'jeremyjiang'
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClinicalProjectsViewSet

cp_list = ClinicalProjectsViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
cp_detail = ClinicalProjectsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    # 'delete': 'destroy'
})

urlpatterns = [
    path('', cp_list, name='cp_list'),
    path('<pk>/', cp_detail, name='cp_detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)