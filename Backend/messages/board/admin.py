from django.contrib import admin

# Register your models here.
from .models import Follower, Message
admin.site.register(Follower)
admin.site.register(Message)
