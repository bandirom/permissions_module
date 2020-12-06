from django.db import models
import subprocess


class Role(models.Model):
    id = models.UUIDField()
    name = models.CharField(max_lenght=50)
    permission = models.ManyToManyField('UserPermission')


class Action(models.Model):
    id = models.UUIDField()
    name = models.CharField(max_lenght=50)
    path_file = models.CharField(help_text='Path to the executable linux/windows script')

    def run_action(self, *args):
        output = subprocess.call([self.path_file, *args])
        return output


class UserPermission(models.Model):
    id = models.AutoField()
    name = models.CharField(max_lenght=50)
    action = models.OneToOneField('Action', on_delete=models.CASCADE)


class User(models.Model):
    id = models.AutoField()
    email = models.EmailField()
    first_name = models.CharField(max_lenght=100)
    last_name = models.CharField(max_length=100)
    user_permissions = models.ManyToManyField('UserPermission')
    role = models.ManyToManyField('Role')
