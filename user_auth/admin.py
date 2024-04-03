from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


# Heading
admin.site.site_header = "Administration | Movie Ratings"

# Group will not show in admin panel
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin class for viewing & adding new user with phone field
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2'),
        }),
    )

    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'is_active', 'is_staff', 'is_superuser')
    list_editable = ('phone', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('username',)
    ordering = ('id',)
