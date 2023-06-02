from django.contrib import admin
from .models import Events


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Events, AuthorAdmin)
