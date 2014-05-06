from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from menu_icons.models import MenuIcon


class MenuIconAdmin(PageExtensionAdmin):
    """
    Adds fields for Menu Icons
    """
    fieldsets = [
        ('Menu Icons - django CMS extension (USELESS IN THE BACKEND)', {
            'fields': ['menu_icon_image', 'menu_icon_url', 'menu_icon_font_awesome']
        }),
    ]

admin.site.register(MenuIcon, MenuIconAdmin)

