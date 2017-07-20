from cms.api import get_page_draft
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils import get_cms_setting
from cms.utils.page_permissions import user_can_change_page
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, NoReverseMatch
from menu_icons.models import MenuIcon


@toolbar_pool.register
class MenuIconToolbar(CMSToolbar):
    model = MenuIcon

    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)

        if not self.page:
            # Nothing to do
            return

        # check global permissions if CMS_PERMISSIONS is active
        if get_cms_setting('PERMISSION'):
            has_global_current_page_change_permission = user_can_change_page(self.request.user, page=self.page)
        else:
            has_global_current_page_change_permission = False

        # check if user has page edit permission
        can_change = self.request.current_page and user_can_change_page(self.request.user, page=self.page)

        if has_global_current_page_change_permission or can_change:
            try:
                menu_icons = MenuIcon.objects.get(extended_object_id=self.page.id)
            except MenuIcon.DoesNotExist:
                menu_icons = None
            try:
                if menu_icons:
                    url = reverse('admin:menu_icons_menuicon_change', args=(menu_icons.pk,))
                else:
                    url = reverse('admin:menu_icons_menuicon_add') + '?extended_object=%s' % self.page.pk
            except NoReverseMatch:
                # not in urls
                pass

            not_edit_mode = not self.toolbar.edit_mode
            current_page_menu = self.toolbar.get_or_create_menu('page')
            current_page_menu.add_modal_item(_('Menu Icon'), url=url, disabled=not_edit_mode, position=0)

