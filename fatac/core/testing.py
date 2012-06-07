from Products.CMFCore.utils import getToolByName

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class FATAC(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import fatac.core
        xmlconfig.file('configure.zcml',
                       fatac.core,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'fatac.core:default')

    def tearDownZope(self, app):
        pass

FATAC_FIXTURE = FATAC()
FATAC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FATAC_FIXTURE,),
    name="FATAC:Integration")
FATAC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FATAC_FIXTURE,),
    name="FATAC:Functional")
