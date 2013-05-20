from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page
from django.contrib import admin
from menu_icons.models import MenuIcon


class MenuIconAdmin(admin.TabularInline):
    """
    Adds fields for Menu Icons
    """
    fieldsets = [
        ('Menu Icons', {
            'fields': ['menu_icon_image', 'menu_icon_url', 'menu_icon_font_awesome']
        }),
    ]
    model = MenuIcon

PageAdmin.inlines.append(MenuIconAdmin)
admin.site.unregister(Page)
admin.site.register(Page, PageAdmin)
