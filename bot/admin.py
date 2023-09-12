from django.contrib import admin

from bot.models import Account, Chat, Command

# Register your models here.
@admin.register(Account)
class PostAdmin(admin.ModelAdmin):
    list_display =("__str__",)

@admin.register(Chat)
class PostAdmin(admin.ModelAdmin):
    list_display =("__str__",)

@admin.register(Command)
class PostAdmin(admin.ModelAdmin):
    list_display =("__str__",)