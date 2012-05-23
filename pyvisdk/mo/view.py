
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class View(BaseEntity):
    '''View is the base class for session-specific view objects. A view is a mechanism
    that supports selection of objects on the server and subsequently, access to
    those objects. To create a view, use the ViewManager methods. A view exists
    until you terminate it by calling the DestroyView method, or until the end of
    the session. Access to a view is limited to the session in which it is
    created.There are three types of views:* ContainerView * ListView *
    InventoryViewA view maintains a view list that contains managed object
    references. You can use a view with the PropertyCollector to retrieve data and
    obtain notification of changes to the virtual environment. For information
    about using views with the PropertyCollector, see the description of
    ViewManager.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.View):
        super(View, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def DestroyView(self):
        '''Destroy this view.
        
        '''
        return self.delegate("DestroyView")()