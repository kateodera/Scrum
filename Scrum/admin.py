from django.contrib import admin
from .models import User, Sprint, Task

# Register your models here.
admin.site.register(User)
admin.site.register(Sprint)
admin.site.register(Task)
