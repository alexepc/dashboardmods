from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu.models import *

# to activate your custom menu add the following to your settings.py:
#
# ADMIN_TOOLS_MENU = 'example.menu.CustomMenu'

class CustomMenu(Menu):
    """
    Custom Menu for example admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children.append(MenuItem(
            title=_('Dashboard'),
            url=reverse('admin:index')
        ))
        self.children.append(AppListMenuItem(
            title=_('Applications'),
            exclude_list=('django.contrib',)
        ))
        self.children.append(AppListMenuItem(
            title=_('Administration'),
            include_list=('django.contrib',)
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass