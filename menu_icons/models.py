from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class MenuIcon(PageExtension):
    """
    Defines Menu Icon fields
    """
    menu_icon_font_awesome = models.CharField(
        max_length=48,
        verbose_name="Menu Icon Font Awesome",
        blank=True,
        null=True
    )
    menu_icon_image = models.ImageField(
        'Menu Icon Image',
        upload_to='menu_icons/',
        blank=True,
        null=True
    )
    menu_icon_url = models.URLField(
        'Menu Icon URL',
        blank=True,
        null=True
    )

extension_pool.register(MenuIcon)

