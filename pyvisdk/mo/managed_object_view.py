
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.view import View

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ManagedObjectView(View):
    '''ManagedObjectView is the base class for view objects that provide access to a
    set of ManagedEntity objects. ManagedObjectView defines a view list; the list
    contains references to objects in the view. To create a view use the
    ViewManager methods.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ManagedObjectView):
        super(ManagedObjectView, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def view(self):
        '''The list of references to objects mapped by this view.'''
        return self.update('view')

    