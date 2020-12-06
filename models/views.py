from django import forms
from .models import User, UserPermission


class GrandPermission:

    user_id = forms.IntegerField()
    permission_id = forms.IntegerField()

    def save(self):
        user = User.objects.get(id=self.user_id)
        permission = UserPermission.objects.get(id=self.permission_id)
        user.user_permissions.add(permission)


class ListUserPermission:

    user_id = forms.IntegerField()

    def list(self, user_id):
        user = User.objects.get(id=self.user_id)
        data = {
            "roles": user.role.all(),
            "permissions": user.user_permissions.all(),
        }
        return data
