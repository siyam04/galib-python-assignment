from django.contrib import admin
from django.contrib.auth.models import User, Group


# Heading
admin.site.site_header = "Administration | Movie Ratings"

# Group will not show in admin panel
admin.site.unregister(Group)
