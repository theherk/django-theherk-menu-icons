from django.db import models
from cms.models.pagemodel import Page


class MenuIcon(models.Model):
    """
    Defines Menu Icon fields
    """
    page = models.OneToOneField(Page)
    menu_icon_font_awesome = models.CharField(
        max_length=48,
        verbose_name="Menu Icon Font Awesome",
        default="icon-",
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
