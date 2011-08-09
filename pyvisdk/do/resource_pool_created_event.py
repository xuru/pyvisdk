
from pyvisdk.do.resource_pool_event import ResourcePoolEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolCreatedEvent(ResourcePoolEvent):
    '''This event records when a new resource pool is created.
    '''
    
    def __init__(self, parent):
        # MUST define these
        super(ResourcePoolCreatedEvent, self).__init__()
    
        self.data['parent'] = parent
    
    
    @property
    def parent(self):
        '''The parent resource pool that new resource pool belongs to.
        '''
        return self.data['parent']

