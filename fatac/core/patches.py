from Acquisition import aq_inner
from plone.app.discussion.browser.conversation import ConversationView


old_enabled = ConversationView.enabled


def enabled(self):
    parent = aq_inner(self.__parent__)
    if parent.portal_type == 'fatac.dummy':
        return True
    return old_enabled(self)
