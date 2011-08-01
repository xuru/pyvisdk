
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class View(BaseEntity):
    '''View is the base class for session-specific view objects. A view is a mechanism
        that supports selection of objects on the server and subsequently, access
        to those objects. To create a view, use the ViewManager methods. A view
        exists until you terminate it by calling the DestroyView method, or until
        the end of the session. Access to a view is limited to the session in
        which it is created.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.View):
        # MUST define these
        super(View, self).__init__(core, name=name, ref=ref, type=type)
    
    
