""" User's admin module """

# Django

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Custom models

from .models import PasswordRetrieval

class PasswordRetrievalInline(admin.StackedInline):
    """ Class to use password retrieval in admin's module """

    model = PasswordRetrieval
    can_delete = False
    verbose_name = 'Password Retrieval'


class UserAdmin(BaseUserAdmin):
    """ Setting user's admin class """

    inlines = (PasswordRetrievalInline,)
    
    list_display = (
        'username',
        'email',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


