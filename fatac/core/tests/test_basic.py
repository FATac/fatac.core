import unittest2 as unittest
from fatac.core.testing import FATAC_FUNCTIONAL_TESTING, FATAC_INTEGRATION_TESTING
from AccessControl import Unauthorized
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import login, logout
from plone.app.testing import setRoles
from plone.testing import z2
from plone.app.testing import applyProfile

import transaction


class FunctionalTest(unittest.TestCase):

    layer = FATAC_FUNCTIONAL_TESTING

    def setUp(self):
        self.browser = z2.Browser(self.layer["app"])

    @property
    def portal(self):
        return self.layer["portal"]

    @property
    def portal_url(self):
        return self.portal.absolute_url()

    def test_create_ghost_container(self):
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        transaction.commit()
        self.browser.open(self.portal_url + "/login_form")

        self.browser.getControl(name="__ac_name").value = TEST_USER_NAME
        self.browser.getControl(name="__ac_password").value = TEST_USER_PASSWORD
        self.browser.getControl(name="submit").click()
        self.assertFalse(self.portal.portal_membership.isAnonymousUser())

        self.browser.open('%s/@@fatac_settings' % self.portal.absolute_url())
        self.browser.getControl(name="form.buttons.save").click()

        self.assertTrue(self.portal.arts.id == 'arts')


class IntegrationTest(unittest.TestCase):

    layer = FATAC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_Groups_folder_created(self):
        self.assertTrue('Groups' in self.portal.objectIds())
