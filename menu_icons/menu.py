from menus.base import Modifier
from menus.menu_pool import menu_pool
from menu_icons.models import MenuIcon


class MenuIconsMod(Modifier):
    """
    Add Menu Icons to the menu nodes
    First check that we are not dealing with breadcrumbs.
    Then attempt to set icons referenced to page id.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        # import ipdb; ipdb.set_trace()
        # if post_cut:
        #     return nodes
        # if breadcrumb:
        #     return nodes
        for node in nodes:
            try:
                # Load Menu Icons into template tags
                # Here lies a bolognapants McGee workaround due
                # to the double publishing feature added in 2.4.
                menu_icons = MenuIcon.objects.get(page=(node.id-1))
                node.menu_icon_image = menu_icons.menu_icon_image
                node.menu_icon_url = menu_icons.menu_icon_url
                node.menu_icon_font_awesome = menu_icons.menu_icon_font_awesome
            except:
                pass

        return nodes

menu_pool.register_modifier(MenuIconsMod)
