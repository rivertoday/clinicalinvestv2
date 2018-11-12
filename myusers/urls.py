from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MyUserList, MyUserDetail, UpdatePassword

urlpatterns = [
    path('', MyUserList.as_view(), name='myuser-list'),
    path('<pk>/', MyUserDetail.as_view(), name='myuser-detail'),
    path('<pk>/changepassword/', UpdatePassword.as_view(), name='myuser-changepassword'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
