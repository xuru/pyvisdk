
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.view import View
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ManagedObjectView(View):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ManagedObjectView):
        # MUST define these
        super(ManagedObjectView, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def view(self):
        '''The list of references to objects mapped by this view.
        '''
        return self.update('view')

