from django.contrib import admin

# from django.contrib import admin

from restaurant_menu.models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")
admin.site.register(Item, MenuItemAdmin)