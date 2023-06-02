from django.contrib import admin
from .models import Organizations


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organizations, AuthorAdmin)
