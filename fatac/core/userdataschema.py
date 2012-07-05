from zope.interface import implements
from zope import schema

from Products.CMFPlone import PloneMessageFactory as _
from fatac.theme import FatacThemeMessageFactory as FATACMF
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import checkEmailAddress
from plone.app.users.browser.personalpreferences import UserDataPanel, PasswordAccountPanel
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


def validateAccept(value):
    if not value == True:
        return False
    return True


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    fullname = schema.TextLine(
        title=_(u'label_full_name', default=u'Full Name'),
        description=_(u'help_full_name_creation',
                      default=u"Enter full name, e.g. John Smith."),
        required=True)

    email = schema.ASCIILine(
        title=_(u'email', default=u'E-mail'),
        description=u'',
        required=True,
        constraint=checkEmailAddress)

    occupation = schema.TextLine(
        title=FATACMF(u'label_occupation', default=u'Occupation'),
        description=FATACMF(u'help_city',
                      default=u"Fill in your occupation or the work you develop."),
        required=True,
        )

    institution = schema.TextLine(
        title=FATACMF(u'label_institution', default=u'Institution'),
        description=FATACMF(u'help_city',
                      default=u"Fill in the institution you represent or work for."),
        required=False,
        )

    city = schema.TextLine(
        title=FATACMF(u'label_city', default=u'City'),
        description=FATACMF(u'help_city',
                      default=u"Fill in the city you live in."),
        required=True,
        )

    home_page = schema.TextLine(
        title=_(u'label_homepage', default=u'Home page'),
        description=_(u'help_homepage',
                      default=u"The URL for your external home page, "
                      "if you have one."),
        required=False)

    accept = schema.Bool(
        title=FATACMF(u'label_accept', default=u'Accept terms of use'),
        description=FATACMF(u'help_accept',
                      default=u"Tick this box to indicate that you have found,"
                      " read and accepted the terms of use for this site. "),
        required=True,
        constraint=validateAccept,
        )


class CustomizedUserDataPanel(UserDataPanel):

    template = ViewPageTemplateFile('browser/profile_form.pt')

    def __init__(self, context, request):
        super(CustomizedUserDataPanel, self).__init__(context, request)
        self.form_fields = self.form_fields.omit('accept', 'location', 'portrait', 'pdelete', 'description')


class CustomizedPasswordAccountPanel(PasswordAccountPanel):

    template = ViewPageTemplateFile('browser/change_password_form.pt')
