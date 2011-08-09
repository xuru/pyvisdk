
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolEventArgument(EntityEventArgument):
    '''The event argument is a ResourcePool object.
    '''
    
    def __init__(self, resourcePool):
        # MUST define these
        super(ResourcePoolEventArgument, self).__init__()
    
        self.data['resourcePool'] = resourcePool
    
    
    @property
    def resourcePool(self):
        '''The ResourcePool object.
        '''
        return self.data['resourcePool']

