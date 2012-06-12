from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType


def crearObjecte(context, id, type_name, title, description, exclude=True, constrains=None):
    pt = getToolByName(context, 'portal_types')
    if not getattr(context, id, False) and type_name in pt.listTypeTitles().keys():
        #creem l'objecte i el publiquem
        _createObjectByType(type_name, context, id)
    #populem l'objecte
    created = context[id]
    doWorkflowAction(created)
    created.setTitle(title)
    created.setDescription(description)
    created._at_creation_flag = False
    created.setExcludeFromNav(exclude)
    if constrains:
        created.setConstrainTypesMode(1)
        if len(constrains) > 1:
            created.setLocallyAllowedTypes(tuple(constrains[0] + constrains[1]))
        else:
            created.setLocallyAllowedTypes(tuple(constrains[0]))
        created.setImmediatelyAddableTypes(tuple(constrains[0]))

    created.reindexObject()
    return created


def doWorkflowAction(context):
    pw = getToolByName(context, "portal_workflow")
    object_workflow = pw.getWorkflowsFor(context)[0].id
    object_status = pw.getStatusOf(object_workflow, context)
    if object_status:
        try:
            pw.doActionFor(context, {'simple_publication_workflow': 'publish'}[object_workflow])
        except:
            pass
