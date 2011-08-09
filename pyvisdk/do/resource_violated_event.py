
from pyvisdk.do.resource_pool_event import ResourcePoolEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourceViolatedEvent(ResourcePoolEvent):
    '''This event records when a conflict with a resource pool's resource configuration
        is detected.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(ResourceViolatedEvent, self).__init__()
    

    
    
