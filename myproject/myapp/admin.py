
from .models import Task
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Unregister default User model
admin.site.unregister(User)

# Customize User admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    search_fields = ('username', 'email')

# Re-register with customization
admin.site.register(User, CustomUserAdmin)

admin.site.register(Task)