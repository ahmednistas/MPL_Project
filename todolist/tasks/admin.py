from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Task
# Register your models here.


admin.site.register(Task)

User = get_user_model()

try:
    admin.site.register(User)
except admin.sites.AlreadyRegistered:
    pass