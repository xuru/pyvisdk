
from pyvisdk.do.resource_pool_event import ResourcePoolEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolMovedEvent(ResourcePoolEvent):
    '''This event records when a resource pool is moved.
    '''
    
    def __init__(self, newParent, oldParent):
        # MUST define these
        super(ResourcePoolMovedEvent, self).__init__()
    
        self.data['newParent'] = newParent
        self.data['oldParent'] = oldParent
    
    
    @property
    def newParent(self):
        '''The new parent of the resource Pool.
        '''
        return self.data['newParent']

    @property
    def oldParent(self):
        '''The old parent of the resource Pool.
        '''
        return self.data['oldParent']

