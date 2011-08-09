
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComputeResourceEventArgument(EntityEventArgument):
    '''The event argument is a ComputeResource object.
    '''
    
    def __init__(self, computeResource):
        # MUST define these
        super(ComputeResourceEventArgument, self).__init__()
    
        self.data['computeResource'] = computeResource
    
    
    @property
    def computeResource(self):
        '''The ComputeResource object.
        '''
        return self.data['computeResource']

