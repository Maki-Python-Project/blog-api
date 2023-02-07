from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from . import models


# admin.site.register(models.Article)
admin.site.register(models.Category)


@admin.register(models.Article)
class ArticleAdmin(GuardedModelAdmin):
    list_display = ("title",)

    def has_module_permission(self, request):
        return super().has_module_permission(request)
