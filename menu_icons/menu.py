from cms import __version__

from menus.base import Modifier
from menus.menu_pool import menu_pool
from menu_icons.models import MenuIcon
from cms.models.pagemodel import Page


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
                if __version__ >= "2.4" and __version__ < "3":  # tested with django-cms at version 2.4.3
                    # Load Menu Icons into template tags
                    # Workaround due to the double publishing feature added in 2.4.
                    # menu icons refers to page marked as "publisher_is_draft"
                    node_page = Page.objects.get(id = node.id)
                    draft_page_id = node_page.id if node_page.publisher_is_draft else node_page.publisher_public_id
                    menu_icons = MenuIcon.objects.get( page = draft_page_id )
                else:
                    menu_icons = MenuIcon.objects.get(page=(node.id))
                    node.menu_icon_image = menu_icons.menu_icon_image
                    node.menu_icon_url = menu_icons.menu_icon_url
                    node.menu_icon_font_awesome = menu_icons.menu_icon_font_awesome
            except:
                pass

        return nodes

menu_pool.register_modifier(MenuIconsMod)
