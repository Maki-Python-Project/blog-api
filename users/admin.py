from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "date_joined",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )


admin.site.register(models.User, CustomUserAdmin)
