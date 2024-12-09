from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "password",
        "phone",
        "tg_nick",
        "city",
    )
    list_filter = ("city",)
    search_fields = ("email", "phone", "tg_nick")