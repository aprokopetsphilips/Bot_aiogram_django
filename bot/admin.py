from django.contrib import admin

from bot.models import Account, Chat


# Register your models here.
@admin.register(Account)
class PostAdmin(admin.ModelAdmin):
    list_display =("__str__",)

@admin.register(Chat)
class PostAdmin(admin.ModelAdmin):
    list_display =("__str__",)

