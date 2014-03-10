from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUser(AbstractUser):

    address = models.TextField(max_length=50)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )



class Rules(models.Model):
    name = models.TextField(max_length=50)

    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
        )


# class Item(models.Model):
#     uploader = models.ForeignKey(User)
#     title = models.TextField(max_length=50)
#     description = models.CharField(max_length=50)
#
#     def can_ship(self, user_obj):
#         """
#         Checks if the given user_obj is the supplier of the item
#         """
#         return self.supplier == user_obj