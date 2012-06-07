import unittest2 as unittest
from fatac.core.testing import FATAC_FUNCTIONAL_TESTING
from AccessControl import Unauthorized
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import login, logout
from plone.app.testing import setRoles
from plone.testing import z2
from plone.app.testing import applyProfile


class FunctionalTest(unittest.TestCase):

    layer = FATAC_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_create_ghost_container(self):
        browser = z2.Browser(self.layer["app"])

        import ipdb;ipdb.set_trace()
        browser.open('%s/@@fatac_settings' % self.portal.absolute_url())
