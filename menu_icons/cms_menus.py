from menus.base import Modifier
from menus.menu_pool import menu_pool
from cms.models.pagemodel import Page
from menu_icons.models import MenuIcon


class MenuIconsMod(Modifier):
    """
    Add Menu Icons to the menu nodes
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        for node in nodes:
            try:
                # Load Menu Icons into template tags
                page=Page.objects.get(pk=node.id)
                #import ipdb; ipdb.set_trace()
                node.menu_icon_image = page.menuicon.menu_icon_image
                node.menu_icon_url = page.menuicon.menu_icon_url
                node.menu_icon_font_awesome = page.menuicon.menu_icon_font_awesome
            except:
                pass

        return nodes

menu_pool.register_modifier(MenuIconsMod)
