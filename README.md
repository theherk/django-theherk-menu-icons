TheHerk Menu Icons
==================

TheHerk Menu Icons is a django CMS navigation modifier that allows attaching icons to menu nodes. These icons can be: a link to an external icon resource, an uploaded icon image file, or by using a class to call a Font Awesome icon.

*note* - If you use this on a Django-cms version prior to 2.4, you will have to modify the menu modifier queryset. It required the most bologna hack ever because of the new oddly behaved double publishing system.

Usage
-----

1. Add "menu_icons" to your INSTALLED_APPS

        INSTALLED_APPS = (
            ...
            'menu_icons',
        )

2. Run `python manage.py migrate menu_icons`.

   Alternately, you could `syncdb` and `migrate --fake`
