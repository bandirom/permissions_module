from django.urls import path
from .views import GrandPermission, ListUserPermission

url_patterns = [
    path('/grand-permission/', GrandPermission),
    path('/permissions/<user_id>/', ListUserPermission),

]

