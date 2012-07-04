from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from Products.CMFPlone.utils import set_own_login_name, safe_unicode
from Products.CMFCore.utils import getToolByName


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def _getProperty(self, name):
        """ PlonePAS encodes all unicode coming from PropertySheets.
            Decode before sending to formlib. """
        value = self.context.getProperty(name, '')
        if value:
            return safe_unicode(value)
        return value

    def get_fullname(self):
        return self._getProperty('fullname')

    def set_fullname(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'fullname': value})

    fullname = property(get_fullname, set_fullname)

    def get_email(self):
        return self._getProperty('email')

    def set_email(self, value):
        if value is None:
            value = ''
        props = getToolByName(self, 'portal_properties').site_properties
        if props.getProperty('use_email_as_login'):
            set_own_login_name(self.context, value)
        return self.context.setMemberProperties({'email': value})

    email = property(get_email, set_email)

    def get_occupation(self):
        return self.context.getProperty('occupation', '')

    def set_occupation(self, value):
        return self.context.setMemberProperties({'occupation': value})
    occupation = property(get_occupation, set_occupation)

    def get_institution(self):
        return self.context.getProperty('institution', '')

    def set_institution(self, value):
        return self.context.setMemberProperties({'institution': value})
    institution = property(get_institution, set_institution)

    def get_city(self):
        return self.context.getProperty('city', '')

    def set_city(self, value):
        return self.context.setMemberProperties({'city': value})
    city = property(get_city, set_city)

    def get_home_page(self):
        return self._getProperty('home_page')

    def set_home_page(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'home_page': value})

    home_page = property(get_home_page, set_home_page)

    def get_accept(self):
        return self.context.getProperty('accept', '')

    def set_accept(self, value):
        return self.context.setMemberProperties({'accept': value})
    accept = property(get_accept, set_accept)
