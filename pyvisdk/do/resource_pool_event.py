
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolEvent(Event):
    '''This event is the base class for all resource pool events.
    '''
    
    def __init__(self, resourcePool):
        # MUST define these
        super(ResourcePoolEvent, self).__init__()
    
        self.data['resourcePool'] = resourcePool
    
    
    @property
    def resourcePool(self):
        '''
        '''
        return self.data['resourcePool']

